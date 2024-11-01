import os
from ctypes import cdll, c_char_p


so_path = "./lib/passwd.so"


def decrypt_passwd(passwd, so_path="./lib/passwd.so"):
    try:
        lib = cdll.LoadLibrary(so_path)
        lib.passedDecrypt.argtypes = [c_char_p]
        lib.passedDecrypt.restype = c_char_p
        password = lib.passedDecrypt(passwd.encode()).decode()
        return password
    except Exception:
        return passwd


def get_sql_connect(db_config: dict):
    db_engine = db_config.get('db_engine')
    db_username = db_config.get('db_username')
    db_pass = decrypt_passwd(db_config.get('db_pass'), so_path)
    db_host = db_config.get('db_host')
    db_port = db_config.get('db_port')
    db_name = db_config.get('db_name')
    return f'{db_engine}://{db_username}:{db_pass}@{db_host}:{db_port}/{db_name}'


class BasicConfig(object):
    def __init__(self, db_config, debug=False):
        self.SQLALCHEMY_DATABASE_URI = get_sql_connect(db_config)

        if debug:
            self.DEBUG = debug

    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # SQLALCHEMY_ENGINE_OPTIONS
    SQLALCHEMY_ENGINE_OPTIONS = {
        # 每次從 Connection Pool 取得連線時，就試著執行一次相當於 SELECT 1 的 SQL ，如果有問題，就可以重新建立新的連線取代失效的連線。
        'pool_pre_ping': True,

        # the lifetime of DBAPI connection
        'pool_recycle': 60,

        # the time to wait for getting a new connection from the connection pool
        'pool_timeout': 100,

        # The size of the pool to be maintained, defaults to 5.
        'pool_size': 10,

        # the number of connections over the pool_size
        'max_overflow': 100,
    }
