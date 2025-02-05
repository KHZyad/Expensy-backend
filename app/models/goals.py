from app.config import supabase

class GoalsModel:
    @staticmethod
    def get_all(user_id):
        return supabase.table("goals").select("*").eq("user_id", user_id).execute().data

    @staticmethod
    def set_goal(data):
        return supabase.table("goals").insert(data).execute().data

    @staticmethod
    def add_to_goal(goal_id, user_id, amount):
        goal = supabase.table("goals").select("*").eq("id", goal_id).eq("user_id", user_id).execute().data
        if not goal:
            return None

        new_amount = float(goal[0]["current_amount"]) + amount
        supabase.table("goals").update({"current_amount": new_amount}).eq("id", goal_id).execute()

        if new_amount >= float(goal[0]["goal_amount"]):
            supabase.table("goals").delete().eq("id", goal_id).execute()
            supabase.table("notifications").insert({
                "user_id": user_id,
                "title": "Goal Achieved",
                "message": f"Congratulations! You have reached your goal: {goal[0]['title']}"
            }).execute()

        return {"current_amount": new_amount, "goal_amount": goal[0]["goal_amount"]}
