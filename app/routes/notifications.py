from flask import Blueprint, request, jsonify
from app.models.notifications import NotificationsModel

notifications_bp = Blueprint("notifications", __name__)

@notifications_bp.route("/", methods=["GET"])
def get_notifications():
    user_id = request.headers.get("user_id")
    return jsonify(NotificationsModel.get_all(user_id)), 200

@notifications_bp.route("/add", methods=["POST"])
def add_notification():
    data = request.json
    return jsonify(NotificationsModel.add_notification(data["user_id"], data["title"], data["message"])), 201
