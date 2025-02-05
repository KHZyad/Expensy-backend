from app.config import supabase

class NotificationsModel:
    @staticmethod
    def get_all(user_id):
        return supabase.table("notifications").select("*").eq("user_id", user_id).execute().data

    @staticmethod
    def add_notification(user_id, title, message):
        data = {"user_id": user_id, "title": title, "message": message}
        return supabase.table("notifications").insert(data).execute().data
