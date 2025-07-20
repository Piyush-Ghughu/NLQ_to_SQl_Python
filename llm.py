import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# API endpoint for Groq
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

# Headers
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}


SYSTEM_PROMPT = """
You are an expert at converting natural language to SQL.
Only use this table: customer with columns: id, name, gender, location, ph_number.
Only return a valid SELECT SQL query. No explanations, no extra symbols, and no formatting — just the raw SQL query.

If the user's input cannot be understood or mapped to a valid SELECT query, respond only with: INVALID_QUERY

"""


def nl_to_sql(nl_query: str) -> str:
    body = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": nl_query}
        ],
        "temperature": 0.2
    }

    response = requests.post(GROQ_URL, headers=HEADERS, json=body)
    response.raise_for_status()

    sql = response.json()["choices"][0]["message"]["content"].strip()
    return sql
