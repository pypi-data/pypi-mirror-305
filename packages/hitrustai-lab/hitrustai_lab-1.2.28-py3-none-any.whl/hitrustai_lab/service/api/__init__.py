import json
import pytz
from flask import jsonify
from datetime import datetime
from importlib import import_module

from ..utils import encrypt_token
from .healthcheck import Healthchecker
from .exception import TokenMissingError, MacValidateError


def get_policy_score(total_score: float):
    return round((total_score*(-2) + 1), 6)


class RouteTool:
    def __init__(
        self,
        model_name: str,
        token: str,
        register_version: str,
        domain='http://127.0.0.1:8080'
    ) -> None:
        self.model_name = model_name
        self.TOKEN = token
        self.REGISTER_VERSION = register_version
        self.domain = domain

    def mac_validation(self, req: dict):
        '''Mac Validate'''
        mac, timestamp = req.get("mac"), req.get("timestamp")
        if mac is None:
            raise TokenMissingError('0103', 'MAC token invalid/missing.')
        elif timestamp is None:
            raise TokenMissingError('0104', 'Timestamp token invalid/missing.')
        else:
            if mac != encrypt_token(self.TOKEN, timestamp):
                raise MacValidateError('9903', 'Mac token validate failed.')

    def jsonify_(self, policy_score, reason, return_code):
        return jsonify({
            "payload": {
                "register_version": self.REGISTER_VERSION,
                "policy_score": policy_score,
                "reason": reason,
            },
            "return_code": return_code
        })

    def add_healthcheck(self, app, url, timestamp="20210623001910", api_name='healthcheck'):
        checker = Healthchecker(
            model_name=self.model_name,
            token=self.TOKEN,
            timestamp=timestamp,
            domain=self.domain,
            url=url
        )

        app = checker.add_healthcheck_url(
            app,
            checker.post_v2,
            f"/model/predict/{self.model_name}/{api_name}",
            api_name=api_name.replace('-', '_')
        )
        return app


class AppInitializer:
    def __init__(
            self,
            kafka_config: object,
            zk_config: object,
            container_env: dict,
            logger
    ):
        self.kafka_config = kafka_config
        self.zk_config = zk_config
        self.container_env = container_env
        self.logger = logger

    @staticmethod
    def register_blueprints(app):
        for module_name in ['predict']:
            module = import_module(f'core.{module_name}.routes')
            app.register_blueprint(module.blueprint)

    def kafka_messgae(self, return_code, reason):
        if self.kafka_config.USE == 'true':
            kafka_info = {
                "return_code": return_code,
                "payload": {
                    "customer_id": self.container_env["customer_id"],
                    "profile_id": self.container_env["profile_id"],
                    "tag": self.container_env["tag"],
                    "model_id": self.container_env["model_id"],
                    "training_id": self.container_env["training_id"],
                    "reason": reason
                }
            }
            kafka_data = json.dumps(kafka_info).encode('utf-8')
            future = self.kafka_config.producer.send(
                self.kafka_config.TOPIC, key=b"MQ003", value=kafka_data)
            self.logger.info("Send mq message sucessfully.")
            return future

    def register_service(self):
        # 註冊服務並發送成功通知
        if self.zk_config.USE == 'true':
            from kazoo.client import KazooClient

            zk = KazooClient(
                hosts=f'{self.zk_config.HOST}:{self.zk_config.PORT}')
            zk.start()

            zk_info = self.container_env.copy()
            zk_info.update({
                "domain": self.zk_config.DOMAIN,
                "apis": ["/api/v1/abnormal_transaction_v2/predict"],
                "create_time": datetime.now().astimezone(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")
            })
            zk_data = json.dumps(zk_info).encode('utf-8')

            # Make sure zk path always exist
            dir = ""
            zk_path = f"{self.zk_config.PATH}/{self.zk_config.NODE}"
            for d in zk_path.split("/"):
                if d == "":
                    continue
                dir += "/" + d
                if not zk.exists(dir):
                    zk.create(dir)

            # Regist service
            if zk.exists(zk_path):
                zk.set(zk_path, zk_data)
                self.logger.info("Regist service successfully.")
            else:
                zk.create(zk_path, zk_data)
                self.logger.info(
                    "Create zk node and regist service successfully.")

        future = self.kafka_messgae("4006", 'Service Success')
