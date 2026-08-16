from flask import Blueprint, request, jsonify
from models import db, User

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/api/profile", methods=["POST"])
def create_profile():

    data = request.get_json()

    user_id = data.get("user_id")

    if not user_id:

        return jsonify({
            "error": "User ID is required"
        }), 400


    # Find the logged-in user

    user = User.query.get(user_id)

    if not user:

        return jsonify({
            "error": "User not found"
        }), 404


    # Update the user's profile

    user.age = data.get("age")
    user.fitness_level = data.get("fitness_level")
    user.goal = data.get("goal")
    user.available_time = data.get("available_time")
    user.movement_type = data.get("movement_type")
    user.equipment = data.get("equipment")


    db.session.commit()


    return jsonify({

        "message": "Profile created successfully!",

        "user_id": user.id

    }), 200