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
        # Convert the string 'date_str' to a datetime object
        try:
            date = datetime.strptime(date_str, '%d %B %Y')  # Example: '13 September 2023'
        except ValueError:
            return {"error": "Invalid date format, should be 'DD Month YYYY'"}, 400
        
        # Get the current timestamp for the creation date
        created_at = datetime.now()

        # Data to be inserted into the table
        data = {
            "user_id": user_id,
            "type": type,
            "amount": amount,
            "vat": vat,
            "method": method,
            "date": date,  # Store as a datetime object
            "created_at": created_at  # Store the creation date
        }

        # Insert the data into the 'transactions' table
        response = supabase.table("transactions").insert(data).execute()
        return response.data  # Return the inserted data
