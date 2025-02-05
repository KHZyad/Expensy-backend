from flask import Blueprint, request, jsonify
from app.utils.auth import verify_supabase_token
from app.models.goals import GoalsModel

goals_bp = Blueprint("goals", __name__)

@goals_bp.route("/", methods=["GET"])
def get_goals():
    token = request.headers.get("Authorization")

    if not token or not token.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid Authorization header"}), 401

    token = token.split(" ")[1]
    user_data = verify_supabase_token(token)

    if not user_data:
        return jsonify({"error": "Invalid or expired token"}), 403

    goals = GoalsModel.get_all(user_data["id"])
    return jsonify(goals), 200
