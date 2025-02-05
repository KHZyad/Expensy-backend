from app.config import supabase

class UsersModel:
    @staticmethod
    def get_or_create_user(user_id, email=None, full_name=None):
        user = supabase.table("users").select("*").eq("id", user_id).execute().data
        if user:
            return user[0]

        # If user does not exist, create one
        data = {"id": user_id, "email": email, "full_name": full_name}
        supabase.table("users").insert(data).execute()
        return data
