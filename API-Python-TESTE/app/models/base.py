from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import __version__ as MarshVersion
from flask_marshmallow import Marshmallow
from flask_restplus import Api
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection
from flask_jwt_extended import JWTManager
from packaging import version
from werkzeug.exceptions import BadRequest, Unauthorized, InternalServerError

db=SQLAlchemy()
ma=Marshmallow()
api = Api(version='1.0', title='Documentação do Back-End', description='Projeto Casa de Apoio Danielle')
jwt = JWTManager()

MarshModelShema=None
if version.parse(MarshVersion) > version.parse("0.10.0"):
    MarshModelShema=ma.SQLAlchemyAutoSchema
else:
    MarshModelShema=ma.ModelSchema

@api.errorhandler(Exception)
def handle_exception(error):
    # erros 400, 401 e 500
    if isinstance(error,BadRequest) or isinstance(error,Unauthorized) or isinstance(error,InternalServerError):
        if  getattr(error, "data", None) and "errors" in error.data.keys():
            dt={}
            for k,v in error.data["errors"].items(): dt[k]=[v]
            if "message" in error.data: dt["message"]=[error.data["message"]]
            error.data=dt
            return error.data, error.code
        elif not getattr(error, "data", None):
            return {"Error":[error.description], "message": [error.description]}, error.code
    return error, error.code

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


