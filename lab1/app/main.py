from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import get_connection
from app.models import init_db
import time


def wait_for_db():
    while True:
        try:
            conn = get_connection()
            conn.close()
            break
        except Exception:
            print("Waiting for DB...")
            time.sleep(1)


@asynccontextmanager
async def lifespan(app: FastAPI):
    wait_for_db()
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/v1/get")
def get_requests():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO requests DEFAULT VALUES")
    cur.execute("SELECT id, created_at FROM requests ORDER BY id")
    rows = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return [
        {"id": r[0], "created_at": str(r[1])}
        for r in rows
    ]
