from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import get_connection
from app.models import init_db
import time
from app.cache.cache_service import get_from_cache, set_to_cache, delete_from_cache
from app.schemas import RequestCreate


def wait_for_db():
    while True:
        try:
            conn = get_connection()
            conn.close()
            break
        except Exception:
            print("waiting for db...")
            time.sleep(1)


@asynccontextmanager
async def lifespan(app: FastAPI):
    wait_for_db()
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/v1/get")
def get_requests():
    cache_key = "all"
    cached = get_from_cache(cache_key)
    if cached:
        print("CACHE HIT")
        return cached

    print("CACHE MISS")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, created_at FROM requests ORDER BY id")
    rows = cur.fetchall()
    
    cur.close()
    conn.close()

    result = [
        {
            "id": r[0],
            "name": r[1],
            "email": r[2],
            "created_at": str(r[3])
        }
        for r in rows
    ]

    set_to_cache(cache_key, result)
    
    return result


@app.post("/api/v1/request")
def create_request(data: RequestCreate):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO requests (name, email) VALUES (%s, %s) RETURNING id, created_at",
        (data.name, data.email)
    )

    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    delete_from_cache("all")
    
    return {
        "id": row[0],
        "created_at": str(row[1]),
        "name": data.name,
        "email": data.email
    }


@app.delete("/api/v1/request/{id}")
def delete_request(id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM requests WHERE id = %s", (id,))
    conn.commit()

    cur.close()
    conn.close()
    delete_from_cache("all")

    return {"status": "deleted"}


@app.delete("/api/v1/clear")
def clear_cache():
    delete_from_cache("all")
    return {"status": "cache cleared"}
