import json
import pytz
import grpc
import time
import decimal
import datetime

from . import datasync_pb2, datasync_pb2_grpc
from ..database.model_handler import ModelHandler


class DateEncoder(json.JSONEncoder):
    """
    自定义类，解决报错：
    TypeError: Object of type "datetime" is not JSON serializable
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.astimezone(pytz.UTC).strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return obj.astimezone(pytz.UTC).strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class DataSyncHandler:
    def __init__(
        self,
        db_settings: dict,
        datasync_config: object,
        logger,
        retry=False
    ) -> None:
        self.DB_NAME = db_settings.get('db_name')
        self.DATASOURCE = datasync_config.DATASOURCE
        self.USE = datasync_config.USE
        self.logger = logger
        self.db_handler = ModelHandler(db_settings=db_settings, logger=logger)
        self.channel = self.build_channel(datasync_config.DOMAIN, retry=retry)
        self.stub = datasync_pb2_grpc.DataSyncStub(self.channel)

    def build_channel(self, datasync_grpc_domain, retry=False):

        if retry:
            service_config_json = json.dumps(
                {
                    "methodConfig": [
                        {
                            # To apply retry to all methods, put [{}] in the "name" field
                            "name": [
                                {"service": "DataSync", "method": "DataSync"}
                            ],
                            "retryPolicy": {
                                "maxAttempts": 5,
                                "initialBackoff": "0.002s",
                                "maxBackoff": "0.01s",
                                "backoffMultiplier": 1,
                                "retryableStatusCodes": ["UNAVAILABLE"],
                            },
                        }
                    ]
                }
            )
            options = []
            options.append(("grpc.enable_retries", 1))
            options.append(("grpc.service_config", service_config_json,))
            channel = grpc.insecure_channel(
                datasync_grpc_domain, options=options)

        else:
            channel = grpc.insecure_channel(datasync_grpc_domain)

        return channel

    def datasync_func(self, data, pk_id=0):
        if self.USE != 'true':
            return None

        sn = data.serial_number
        try:
            output = dict()
            output["data_source"] = self.DATASOURCE
            output["schema"] = self.DB_NAME
            output["table"] = data.__tablename__
            output["payload"] = {x.name: getattr(
                data, x.name) for x in data.__table__.columns}
            output["pk_id"] = pk_id

            request = datasync_pb2.DataSyncRequest(
                value=json.dumps(output, cls=DateEncoder))
            response = self.stub.DataSync(request)
            response = json.loads(response.value)
            self.logger.info(
                f'[{sn}]DataSync {data.__tablename__} Result: {response["reason"][0]}')

        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.CANCELLED:
                self.logger.error(
                    f"[{sn}]DataSync Catch an exception: DataSync Status Canceled")
            elif rpc_error.code() == grpc.StatusCode.UNAVAILABLE:
                self.logger.error(
                    f"[{sn}]DataSync Catch an exception: DataSync Connection Unavaliable")

        except:
            self.logger.exception(f"[{sn}]DataSync Catch an exception:")

    def save_data_and_sync(self, data_type='info', pk_id=None, **data):
        sn = data.get('serial_number', 'UnknownSN')

        t_start_save = time.time()
        self.logger.info(f"[{sn}][ToDB][Start]")
        datasync_content = self.db_handler.save_data(data_type, **data)
        duration = 1000*round(time.time()-t_start_save, 3)
        self.logger.info(f"[{sn}][ToDB][End][{duration}]")

        if datasync_content:
            self.logger.info(f"[{sn}]Datasync flow : {data_type}")
            pk_id_ = pk_id if data_type == 'result' else datasync_content.pk_id

            t_start_ds = time.time()
            self.logger.info(f"[{sn}][DataSync][Start]")
            self.datasync_func(datasync_content, pk_id=pk_id_)
            duration = 1000*round(time.time()-t_start_ds, 3)
            self.logger.info(f"[{sn}][DataSync][End][{duration}]")
            return pk_id_
