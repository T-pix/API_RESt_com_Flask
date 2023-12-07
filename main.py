from flask import Flask, request, jsonify
from db import gpus

app = Flask(__name__)


@app.route("/gpus", methods=["GET"])
def get_gpus():
    return gpus


@app.route("/gpus", methods=["POST"])
def create_gpus():
    gpus.append(request.json)
    return jsonify(message="Gpu adicionada com sucesso")


app.run()
