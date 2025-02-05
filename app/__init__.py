from flask import Flask
from app.routes import users, transactions, reminders, goals, notifications

def create_app():
    app = Flask(__name__)

    app.register_blueprint(users.users_bp, url_prefix="/api/users")
    app.register_blueprint(transactions.transactions_bp, url_prefix="/api/transactions")
    app.register_blueprint(reminders.reminders_bp, url_prefix="/api/reminders")
    app.register_blueprint(goals.goals_bp, url_prefix="/api/goals")
    app.register_blueprint(notifications.notifications_bp, url_prefix="/api/notifications")

    @app.route("/")
    def index():
        return "Expenssy Backend is Running!"

    return app
