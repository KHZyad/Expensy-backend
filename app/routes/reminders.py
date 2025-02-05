from flask import Blueprint, request, jsonify
from app.models.reminders import RemindersModel

reminders_bp = Blueprint("reminders", __name__)

@reminders_bp.route("/", methods=["GET"])
def get_reminders():
    user_id = request.headers.get("user_id")
    return jsonify(RemindersModel.get_all(user_id)), 200

@reminders_bp.route("/add", methods=["POST"])
def add_reminder():
    data = request.json
    return jsonify(RemindersModel.add_reminder(data["user_id"], data["title"], data["amount"], data["due_date"])), 201
