from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Gereserveerd! Melding gemaakt bij NCSC."
