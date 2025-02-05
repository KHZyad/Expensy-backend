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
    def add_transaction(data):
        return supabase.table("transactions").insert(data).execute().data

    @staticmethod
    def get_statistics(user_id):
        transactions = TransactionsModel.get_all(user_id)
        expenses = sum([float(t["amount"]) for t in transactions if float(t["amount"]) < 0])
        income = sum([float(t["amount"]) for t in transactions if float(t["amount"]) > 0])
        return {"total_income": income, "total_expense": expenses, "balance": income + expenses}
