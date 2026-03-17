from flask import *
from dotenv import dotenv_values

userdata = dotenv_values()

app = Flask(__name__)

@app.route("/")
def route_index():
    return render_template("index.html")

@app.route("/comando/<id_utente>", methods=["GET"])
def post_comando(id_utente):
    return "ciao " + id_utente

app.run(port=5000, debug=True)