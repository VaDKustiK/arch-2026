import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "default"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432")
    )