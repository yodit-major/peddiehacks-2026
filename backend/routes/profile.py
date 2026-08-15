from flask import Blueprint, request, jsonify
from models import db, User

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/api/profile", methods=["POST"])
def create_profile():
    data = request.get_json()

    user = User(
        age=data["age"],
        fitness_level=data["fitness_level"],
        goal=data["goal"],
        available_time=data["available_time"],
        movement_type=data["movement_type"],
        equipment=data.get("equipment")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Profile created successfully!",
        "user_id": user.id
    }), 201