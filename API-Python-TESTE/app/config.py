import os, uuid, datetime

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or uuid.uuid4().hex
    DEBUG = True
    CSRF_ENABLED = True
    GET_PER_PAGE = int(os.environ.get("GET_PER_PAGE", 50))
    DATETIME_FORMAT= '%Y-%m-%d %H:%M' ## ISO format. Usado no Model 
    DATE_FORMAT='%Y-%m-%d' ## ISO format. Usado no Model 

class Configdb(Config):
    def __init__(self,): super().__init__(self)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class JWTConfig(Config):
    JWT_SECRET_KEY = Config.SECRET_KEY
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SECURE = True # __init__.is_production change this field...
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_IN_COOKIES = False
    JWT_CSRF_CHECK_FORM = True
    WTF_CSRF_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES=datetime.timedelta(minutes=60*12)
    JWT_REFRESH_TOKEN_EXPIRES=datetime.timedelta(minutes=60*12)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access',] #'refresh']
    def __init__(self,): super().__init__(self)


