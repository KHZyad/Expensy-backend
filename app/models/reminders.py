from app.config import supabase

class RemindersModel:
    @staticmethod
    def get_all(user_id):
        return supabase.table("reminders").select("*").eq("user_id", user_id).execute().data

    @staticmethod
    def add_reminder(user_id, title, amount, due_date):
        data = {"user_id": user_id, "title": title, "amount": amount, "due_date": due_date}
        return supabase.table("reminders").insert(data).execute().data

    @staticmethod
    def update_reminder(reminder_id, user_id, data):
        return supabase.table("reminders").update(data).eq("id", reminder_id).eq("user_id", user_id).execute().data

    @staticmethod
    def delete_reminder(reminder_id, user_id):
        return supabase.table("reminders").delete().eq("id", reminder_id).eq("user_id", user_id).execute().data
