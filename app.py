from flask import Flask, render_template
import random

app = Flask(__name__)

# List of greetings
greetings = [
    ("Hello", "English"),
    ("Hola", "Spanish"),
    ("Bonjour", "French"),
    ("Ciao", "Italian"),
    ("Hallo", "German"),
    ("Olá", "Portuguese"),
    ("Привет", "Russian"),
    ("你好", "Chinese"),
    ("こんにちは", "Japanese"),
    ("안녕하세요", "Korean")
]

# ---- Counter Service (TEMPORARY - LOCAL ONLY) ----
_counter = 0

def get_next_counter():
    global _counter
    _counter += 1
    return _counter
# -----------------------------------------------

@app.route("/")
def home():
    greeting, language = random.choice(greetings)
    visit_count = get_next_counter()

    return render_template(
        "index.html",
        greeting=greeting,
        language=language,
        visit_count=visit_count
    )


if __name__ == "__main__":
    app.run(debug=True)
