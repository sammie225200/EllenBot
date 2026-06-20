from app.db import supabase

def search_quotes(topic):

    result = (
        supabase
        .table("egw_quotes")
        .select("*")
        .ilike("topic", f"%{topic}%")
        .limit(5)
        .execute()
    )

    return result.data