from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from db import execute_query
from llm import nl_to_sql 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="frontpart/build/static"), name="static")

@app.get("/")
def serve_react_index():
    return FileResponse("frontpart/build/index.html")

@app.post("/query")
async def query_handler(request: Request):
    data = await request.json()
    nl_query = data.get("query", "").strip()

    if not nl_query:
        return {
            "sql": None,
            "result": [],
            "error": None,
            "message": "❗Please enter a valid question."
        }

    greetings = [
        "hi", "hello", "hey", "hii", "helloo", "yo", "what's up",
        "hola", "namaste", "sup", "greetings", "bonjour", "howdy"
    ]
    if any(greet in nl_query.lower() for greet in greetings):
        return {
            "sql": None,
            "result": [],
            "error": None,
            "message": "👋 Hi! What can I help you find in the database?"
        }

    try:
        sql = nl_to_sql(nl_query)

        invalid_sql = not sql or not sql.lower().startswith("select")


        if invalid_sql:
            return {
                "sql": sql,
                "result": [],
                "error": None,
                "message": "❌ Couldn't understand your query.\n👋 Try asking something like: who lives in Mumbai?"
            }

        result = execute_query(sql)
        return {"sql": sql, "result": result, "error": None}

    except Exception as e:
        return {
            "sql": None,
            "result": [],
            "error": str(e),
            "message": "🚨 Something went wrong while processing your request."
        }
