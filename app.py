from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    # Flask app
    from flask import Flask
    from config import Config

    app = Flask(__name__)
    app.config.from_object(Config)

    # init db
    db.init_app(app)

    # migrating system
    from flask_migrate import Migrate
    migrate = Migrate(app, db)

    # login system
    from flask_login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    from data.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query_by(id=user_id)

    # rest api
    from flask_restful import Api
    api = Api(app)

    from resources.receipts import ReceiptsListResource, ReceiptsResource
    from resources.users import UsersListResource, UsersResource

    api.add_resource(ReceiptsListResource, "/api/v2/receipts")
    api.add_resource(ReceiptsResource, "/api/v2/receipts/<int:receipt_id>")
    api.add_resource(UsersListResource, "/api/v2/users")
    api.add_resource(UsersResource, "/api/v2/users/<int:phone>")

    return app
