"""
Copyright (c) 2026 Himangshu Pan

Author: Himangshu Pan (0xSh3ru)
Project: HTTP Methods Demo
Repository: https://github.com/0xSh3ru/http-methods-demo

SPDX-License-Identifier: MIT
"""
from flask import Flask, request, Response, jsonify, make_response
import json
import os

app = Flask(__name__)

DB = "data.json"


def load_data():
    if not os.path.exists(DB):
        with open(DB, "w") as f:
            json.dump([], f)

    with open(DB, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DB, "w") as f:
        json.dump(data, f, indent=4)


# ------------------------
# GET
# ------------------------

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(load_data())


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    users = load_data()

    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404


# ------------------------
# POST
# ------------------------

@app.route("/users", methods=["POST"])
def create_user():

    users = load_data()

    body = request.json

    new_user = {
        "id": len(users) + 1,
        "name": body["name"],
        "email": body["email"]
    }

    users.append(new_user)
    save_data(users)

    return jsonify(new_user), 201


# ------------------------
# PUT
# ------------------------

@app.route("/users/<int:user_id>", methods=["PUT"])
def replace_user(user_id):

    users = load_data()

    body = request.json

    for i, user in enumerate(users):

        if user["id"] == user_id:

            users[i] = {
                "id": user_id,
                "name": body["name"],
                "email": body["email"]
            }

            save_data(users)

            return jsonify(users[i])

    return jsonify({"error": "Not Found"}), 404


# ------------------------
# PATCH
# ------------------------

@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_user(user_id):

    users = load_data()

    body = request.json

    for user in users:

        if user["id"] == user_id:

            user.update(body)

            save_data(users)

            return jsonify(user)

    return jsonify({"error": "Not Found"}), 404


# ------------------------
# DELETE
# ------------------------

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    users = load_data()

    users = [u for u in users if u["id"] != user_id]

    save_data(users)

    return "", 204


# ------------------------
# HEAD
# ------------------------

@app.route("/health", methods=["GET", "HEAD"])
def health():
    return jsonify({"status": "running"})


# ------------------------
# OPTIONS
# ------------------------

@app.route("/methods", methods=["OPTIONS"])
def methods():

    response = make_response()

    response.headers["Allow"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD, QUERY"

    return response

@app.route("/users/search", methods=["QUERY"])
def query_users():

    users = load_data()

    body = request.get_json(silent=True) or {}

    results = users

    if "name" in body:
        results = [
            user for user in results
            if body["name"].lower() in user["name"].lower()
        ]

    if "email" in body:
        results = [
            user for user in results
            if body["email"].lower() in user["email"].lower()
        ]

    return jsonify(results)

@app.route("/trace", methods=["TRACE"])
def trace():

    lines = []

    # Request Line
    lines.append(
        f"{request.method} {request.full_path} HTTP/1.1"
    )

    # Headers
    for key, value in request.headers.items():
        lines.append(f"{key}: {value}")

    lines.append("")

    # Body
    body = request.get_data(as_text=True)

    if body:
        lines.append(body)

    return Response(
        "\r\n".join(lines),
        status=200,
        mimetype="message/http"
    )
if __name__ == "__main__":
    app.run(debug=True)
