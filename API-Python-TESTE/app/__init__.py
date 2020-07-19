import os
from flask import Flask
from flask_migrate import Migrate
from flask import Blueprint
from .util.LocalFunctions import CustomJSONEncoder, CustomJSONDecoder
from .util.JWTErrorMessages import register_jwt_callbacks


def create_app():
    root_p=os.path.join(os.path.dirname(__file__), 'webfiles')
    app = Flask(__name__, root_path=root_p, \
        template_folder=os.path.join(root_p,'templates'), \
        static_folder=os.path.join(root_p,'static'))
    app.json_encoder = CustomJSONEncoder
    app.json_decoder = CustomJSONDecoder

    from .config import Config, Configdb, JWTConfig
    app.config.from_object(Config)
    app.config.from_object(Configdb)
    app.config.from_object(JWTConfig)
    app.root_path = root_p
    
    from .models.base import db, ma, api, jwt 
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)

    from .routes.teste import simple_page
    app.register_blueprint(simple_page)

    jwt._set_error_handler_callbacks(api)
    register_jwt_callbacks()
    
    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
