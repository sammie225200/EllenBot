from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.search import search_quotes
from app.groq_client import ask_groq

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check
@app.get("/")
async def home():
    return {
        "status": "ok",
        "message": "EGW Adventist AI running with Groq + Supabase"
    }


# Main endpoint
@app.post("/ask")
async def ask(request: dict):

    question = request.get("question")

    if not question:
        return {"error": "Question is required"}

    # 1. Search EGW dataset
    quotes = search_quotes(question)

    # 2. Build context
    if quotes:
        context = "\n\n".join([
            f"{q.get('book', '')}: {q.get('quote', '')}"
            for q in quotes
        ])
    else:
        context = "No exact EGW match found. Answer using general Adventist principles."

    # 3. Get AI response (Groq)
    answer = ask_groq(question, context)

    # 4. Return response
    return {
        "question": question,
        "answer": answer,
        "sources": quotes
    }