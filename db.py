import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MYSQL_USER_NAME =  os.getenv("MYSQL_USER_NAME")
MYSQL_USER_PASSWORD =  os.getenv("MYSQL_PASSWORD")
MYSQL_USER_DATABASE =  os.getenv("MYSQL_DATABASE_NAME")


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user=MYSQL_USER_NAME,
        password=MYSQL_USER_PASSWORD,
        database=MYSQL_USER_DATABASE
    )

def execute_query(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
