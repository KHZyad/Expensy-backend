from datetime import datetime
from app.config import supabase

class TransactionsModel:
    @staticmethod
    def get_all(user_id):
        return supabase.table("transactions").select("*").eq("user_id", user_id).execute().data

    @staticmethod
    def get_expenses(user_id):
        return supabase.table("transactions").select("*").eq("user_id", user_id).lt("amount", 0).execute().data

    @staticmethod
    def get_incomes(user_id):
        return supabase.table("transactions").select("*").eq("user_id", user_id).gt("amount", 0).execute().data

    @staticmethod
    def add_transaction(user_id, type, amount, vat, method, date_str):
        # Check if date_str is already a datetime object
        if isinstance(date_str, datetime):
            date = date_str  # If it's already a datetime object, use it directly
        else:
            # Otherwise, try to convert it from a string
            try:
                date = datetime.strptime(date_str, '%d %B %Y')  # Example: '13 September 2023'
            except ValueError:
                return {"error": "Invalid date format, should be 'DD Month YYYY'"}, 400

        # Convert datetime objects to ISO 8601 format strings for compatibility with JSON
        date_str_iso = date.isoformat()
        created_at = datetime.now().isoformat()

        data = {
            "user_id": user_id,
            "type": type,
            "amount": amount,
            "vat": vat,
            "method": method,
            "date": date_str_iso,  
            "created_at": created_at  
        }

        response = supabase.table("transactions").insert(data).execute()
        return response.data
