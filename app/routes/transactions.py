from flask import Blueprint, request, jsonify
from app.models.transactions import TransactionsModel

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/", methods=["GET"])
def get_transactions():
    user_id = request.headers.get("user_id")
    return jsonify(TransactionsModel.get_all(user_id)), 200

@transactions_bp.route("/expenses", methods=["GET"])
def get_expenses():
    user_id = request.headers.get("user_id")
    return jsonify(TransactionsModel.get_expenses(user_id)), 200

@transactions_bp.route("/incomes", methods=["GET"])
def get_incomes():
    user_id = request.headers.get("user_id")
    return jsonify(TransactionsModel.get_incomes(user_id)), 200

@transactions_bp.route("/add", methods=["POST"])
def add_transaction():
    data = request.json
    user_id = data.get("user_id")
    type = data.get("type")
    amount = data.get("amount")

    if not user_id or not type or not amount:
        return jsonify({"error": "Missing required fields"}), 400

    return jsonify(TransactionsModel.add_transaction(user_id, type, amount)), 201
