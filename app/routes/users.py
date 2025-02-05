from flask import Blueprint, request, jsonify
from app.models.users import UsersModel

users_bp = Blueprint("users", __name__)

@users_bp.route("/check", methods=["POST"])
def check_user():
    data = request.json
    user_id = data.get("user_id")
    email = data.get("email")
    full_name = data.get("full_name")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    user = UsersModel.get_or_create_user(user_id, email, full_name)
    return jsonify(user), 200
