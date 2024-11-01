import time
import redis
import pickle
from rediscluster import RedisCluster


class RedisTools:
    def __init__(
        self,
        redis_config,
        redis_key='card_abnormal_predict',
        logger=None
    ):
        self.REDIS_CONFIG = redis_config
        self.REDIS_KEY = redis_key
        self.REDIS_MODE = redis_config.MODE if redis_config else 'local'
        self.TIME_EXPIRE = 7*86400

        self.redis_client = self.init_client()
        self.redis_data = {}
        self.logger = logger

    def init_client(self):
        '''Initialize  Redis/Codis by config settings'''

        if self.REDIS_CONFIG is not None:
            mode = self.REDIS_CONFIG.MODE
            if mode == 'codis':
                host, port = self.REDIS_CONFIG.NODE.split(":")
                return redis.Redis(
                    host=host,
                    port=port,
                    password=self.REDIS_CONFIG.PASSWD,
                    decode_responses=False
                )
            elif mode == 'redis':
                redis_servers = []
                redis_nodes = self.REDIS_CONFIG.NODE.split(",")
                for node in redis_nodes:
                    redis_host, redis_port = node.split(":")
                    redis_servers.append({
                        "host": redis_host,
                        "port": redis_port
                    })
                try:

                    return RedisCluster(startup_nodes=redis_servers, password=self.REDIS_CONFIG.PASSWD)
                except:
                    self.logger.exception('RedisCluster Catch an exception:')
                    return None
        return None

    def _progress_bar(self, N, i):
        n = i+1
        progress = f"\r|{'█'*int(n*50/N)}{' '*(50-int(n*50/N))} | {n}/{N} ({round(n/N*100, 2)})%"
        print(progress, end='')

    def _data2byte(self, data):
        return pickle.dumps(data)

    def to_redis(self, data: dict):
        '''insert data to Redis at a time'''

        N = len(data)

        if self.REDIS_MODE == 'local':
            for k, v in data.items():
                key = f'{self.REDIS_KEY}:{k}'
                if key in self.redis_data:
                    if isinstance(self.redis_data[key], dict):
                        self.redis_data[key].update(v)
                    elif v:
                        self.redis_data[key] = list(
                            set(self.redis_data[key]+v))
                elif v:
                    self.redis_data[key] = v
        else:
            if N > 1:
                pipe = self.redis_client.pipeline()

                for k, v in data.items():
                    key = f'{self.REDIS_KEY}:{k}'
                    if v:
                        pipe.set(key, self._data2byte(v))
                        pipe.expire(key, time=self.TIME_EXPIRE)

                pipe.execute()

            else:
                for c in data:
                    key = f'{self.REDIS_KEY}:{c}'
                    self.redis_client.set(key, self._data2byte(data[c]))
                    self.redis_client.expire(key, time=self.TIME_EXPIRE)

    def query(self, sn, key):
        '''query data from redis'''

        key_ = f"{self.REDIS_KEY}:{key}"
        if self.REDIS_MODE == 'local':
            if key_ in self.redis_data:
                return self.redis_data[key_]
            return None
        else:
            n = 0
            while n < 5:
                try:
                    data = self.redis_client.get(key_)
                    break
                except:
                    n += 1
                    self.logger.error(
                        f"[{sn}]Cannot connect to {self.REDIS_MODE}, reconnect ({n}/5).")
                    self.redis_client = self.init_client()
                    time.sleep(1)

            if n == 5:
                return f'[{sn}]{self.REDIS_MODE.capitalize()}ConnectionError'

            try:
                return pickle.loads(data)
            except TypeError:
                return None

    def delete_keys(self, keys: list):
        '''delete data stored in Redis by key'''

        for k in keys:
            if self.REDIS_MODE == 'local':
                self.redis_data.pop(k)
            else:
                self.redis_client.delete(k)

    def clear_all(self):
        '''delete all data stored in Redis'''

        if self.REDIS_MODE == 'local':
            self.redis_data = {}
        else:
            self.redis_client.delete(*self.redis_client.keys())

    def memory_usage(self):
        '''check Redis memory usage'''
        usage = self.redis_client.info()
        usage1 = usage['192.168.10.202:7000']['used_memory']/2**20
        usage2 = usage['192.168.10.202:7001']['used_memory']/2**20
        usage3 = usage['192.168.10.202:7002']['used_memory']/2**20

        print(f'total keys = {len(self.redis_client.keys())}')
        print(f"used_memory of 192.168.10.202:7000 = {usage1} MB")
        print(f"used_memory of 192.168.10.202:7001 = {usage2} MB")
        print(f"used_memory of 192.168.10.202:7002 = {usage3} MB")
        print(
            f"total used_memory = {usage1+usage2+usage3} MB")
