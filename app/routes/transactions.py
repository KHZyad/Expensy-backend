from flask import Blueprint, request, jsonify
from app.models.transactions import TransactionsModel

# Initialize the Blueprint for transaction-related routes
transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route("/", methods=["GET"])
def get_transactions():
    user_id = request.headers.get("user_id")
    
    # Handle missing user_id in headers
    if not user_id:
        return jsonify({"error": "Missing 'user_id' in headers"}), 400

    # Retrieve all transactions for the user
    transactions = TransactionsModel.get_all(user_id)
    return jsonify(transactions), 200

@transactions_bp.route("/expenses", methods=["GET"])
def get_expenses():
    user_id = request.headers.get("user_id")
    
    # Handle missing user_id in headers
    if not user_id:
        return jsonify({"error": "Missing 'user_id' in headers"}), 400

    # Retrieve all expenses for the user
    expenses = TransactionsModel.get_expenses(user_id)
    return jsonify(expenses), 200

@transactions_bp.route("/incomes", methods=["GET"])
def get_incomes():
    user_id = request.headers.get("user_id")
    
    # Handle missing user_id in headers
    if not user_id:
        return jsonify({"error": "Missing 'user_id' in headers"}), 400

    # Retrieve all incomes for the user
    incomes = TransactionsModel.get_incomes(user_id)
    return jsonify(incomes), 200

@transactions_bp.route("/add", methods=["POST"])
def add_transaction():
    data = request.json
    user_id = data.get("user_id")
    type = data.get("type")
    amount = data.get("amount")
    vat = data.get("vat")
    method = data.get("method")
    date_str = data.get("date")  # Date as string

    # Validate that required fields are provided
    if not all([user_id, type, amount, vat, method, date_str]):
        return jsonify({"error": "Missing required fields"}), 400

    # Add the transaction to the database
    transaction = TransactionsModel.add_transaction(user_id, type, amount, vat, method, date_str)

    # Handle possible errors from the add_transaction method
    if "error" in transaction:
        return jsonify(transaction), 400

    return jsonify(transaction), 201