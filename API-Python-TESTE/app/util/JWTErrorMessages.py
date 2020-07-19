from ..models.base import jwt
from werkzeug.exceptions import Unauthorized

def register_jwt_callbacks():
    @jwt.revoked_token_loader
    def jwt_revoked_token_loader_callback():
        raise Unauthorized("Token has been revoked")
    @jwt.invalid_token_loader
    def jwt_invalid_token_loader_callback(self):
        raise Unauthorized("Your auth token or CSRF token are invalid")
    @jwt.unauthorized_loader
    def jwt_unauthorized_callback(self):
        raise Unauthorized("Your auth token or CSRF token are missing")
    @jwt.expired_token_loader
    def jwt_expired_token_callback(self): 
        raise Unauthorized("Your auth token has expired")
    return None