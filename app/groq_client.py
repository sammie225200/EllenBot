from openai import OpenAI
from app.config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPT = """
You are an Adventist assistant.
Use provided context (Ellen G. White writings) only.
Do not hallucinate quotes.
"""

def ask_groq(question, context):

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": f"""
QUESTION:
{question}

CONTEXT:
{context}
"""
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("Groq error:", e)
        return f"AI temporarily unavailable.\n\n{context}"