from flask import Flask, jsonify
from db import get_connection
from models import init_db
import os
import time

app = Flask(__name__)

@app.route("/api/v1/get", methods=["GET"])
def get_requests():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO requests DEFAULT VALUES")
    cur.execute("SELECT id, created_at FROM requests ORDER BY id")
    rows = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()

    return jsonify([
        {"id": r[0], "created_at": str(r[1])}
        for r in rows
    ])


def wait_for_db():
    while True:
        try:
            conn = get_connection()
            conn.close()
            break
        except Exception:
            print("Waiting for DB...")
            time.sleep(1)


if __name__ == "__main__":
    wait_for_db()
    init_db()

    port = int(os.getenv("SERVER_PORT", 8080))
    app.run(host="0.0.0.0", port=port)