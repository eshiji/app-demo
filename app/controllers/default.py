from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def test_bootstrap():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "app-demo is runnning..."}

@app.route('/handle_data', methods=['POST'])
def handle_data():
    return render_template("submit.html")
    # your code
    # return a response