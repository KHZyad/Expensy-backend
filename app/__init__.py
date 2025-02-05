from flask import Flask
from flask_cors import CORS
from app.routes.transactions import transactions_bp
from app.routes.reminders import reminders_bp
from app.routes.goals import goals_bp
from app.routes.notifications import notifications_bp
from app.routes.users import users_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(transactions_bp, url_prefix="/transactions")
    app.register_blueprint(reminders_bp, url_prefix="/reminders")
    app.register_blueprint(goals_bp, url_prefix="/goals")
    app.register_blueprint(notifications_bp, url_prefix="/notifications")
    app.register_blueprint(users_bp, url_prefix="/users")

    return app
