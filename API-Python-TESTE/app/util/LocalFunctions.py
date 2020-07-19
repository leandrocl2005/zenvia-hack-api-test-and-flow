import datetime
from re import search, sub
from unicodedata import normalize
from sqlalchemy.orm import MapperExtension
from flask.json import JSONEncoder, JSONDecoder
from ..config import Config


class CustomJSONEncoder(JSONEncoder): 
    def default(self, obj):
        try:
            if isinstance(obj, (datetime.datetime)):
                return obj.strftime(Config.DATETIME_FORMAT)
            elif isinstance(obj, (datetime.date)):
                return obj.strftime(Config.DATE_FORMAT)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

class CustomJSONDecoder(JSONDecoder): 
    def default(self, obj):
        try:
            if isinstance(obj, (datetime.datetime)):
                return obj.strftime(Config.DATETIME_FORMAT)
            elif isinstance(obj, (datetime.date)):
                return obj.strftime(Config.DATE_FORMAT)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONDecoder.default(self, obj)


