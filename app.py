from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

from flask import Flask, jsonify, request
import psycopg2
import random
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="Fatemeh123",
        port=5432
    )

# Temporary in-memory counter
user_counters = {}

@app.route("/events/random", methods=["GET"])
def random_event():
    user_id = request.args.get("user_id", "user1")

    if user_id not in user_counters:
        user_counters[user_id] = 0

    user_counters[user_id] += 1
    random_value = random.randint(1, 100)

    user_agent = request.headers.get("User-Agent")
    ip_address = request.remote_addr
    endpoint = request.path
    method = request.method

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO events
        (user_id, random_value, user_counter, user_agent, ip_address, endpoint, request_method)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            user_id,
            random_value,
            user_counters[user_id],
            user_agent,
            ip_address,
            endpoint,
            method
        )
    )

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "user_id": user_id,
        "random_value": random_value,
        "counter": user_counters[user_id],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

if __name__ == "__main__":
    app.run(debug=True)



