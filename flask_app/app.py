import random
from datetime import datetime
from flask import Flask, request

from utils.s3_logger import log_event_to_s3

app = Flask(__name__)

# ----------- Data -----------
greetings = [
    "Hello", "Hola", "Bonjour", "Ciao", "Hallo",
    "Olá", "Привет", "你好", "こんにちは", "안녕하세요"
]

visit_count = 0

# ----------- Route -----------
@app.route("/")
def home():
    global visit_count
    visit_count += 1

    greeting = random.choice(greetings)

    log_data = {
        "ip": request.remote_addr,
        "user_agent": request.headers.get("User-Agent"),
        "path": request.path,
        "method": request.method,
        "greeting": greeting,
        "visit_count": visit_count,
        "timestamp": datetime.utcnow().isoformat()
    }

    log_event_to_s3(log_data)

    return f"{greeting}, user {visit_count}!"

# ----------- Run -----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

