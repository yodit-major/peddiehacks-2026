from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/api/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Check required fields
    if not username or not password:

        return jsonify({
            "error": "Username and password are required"
        }), 400

    # Check username length
    if len(username) < 3:

        return jsonify({
            "error": "Username must be at least 3 characters"
        }), 400

    # Check password length
    if len(password) < 6:

        return jsonify({
            "error": "Password must be at least 6 characters"
        }), 400

    # Check if username already exists
    existing_user = User.query.filter_by(
        username=username
    ).first()

    if existing_user:

        return jsonify({
            "error": "Username already exists"
        }), 409

    # Hash password
    password_hash = generate_password_hash(
        password
    )

    # Create user
    user = User(
        username=username,
        password_hash=password_hash
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Account created successfully!",
        "user_id": user.id,
        "username": user.username
    }), 201
@auth_bp.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:

        return jsonify({
            "error": "Username and password are required"
        }), 400

    user = User.query.filter_by(
        username=username
    ).first()

    if not user:

        return jsonify({
            "error": "Invalid username or password"
        }), 401

    if not check_password_hash(
        user.password_hash,
        password
    ):

        return jsonify({
            "error": "Invalid username or password"
        }), 401

    return jsonify({
        "message": "Login successful!",
        "user_id": user.id,
        "username": user.username
    }), 200