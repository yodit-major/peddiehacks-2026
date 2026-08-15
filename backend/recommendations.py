from flask import Blueprint, request, jsonify
from models import Activity

recommendations_bp = Blueprint("recommendations", __name__)


@recommendations_bp.route("/api/recommendations", methods=["GET"])
def get_recommendations():

    movement_type = request.args.get("movement_type")
    difficulty = request.args.get("difficulty")
    available_time = request.args.get("available_time", type=int)
    equipment = request.args.get("equipment")

    query = Activity.query

    # Match the user's movement condition
    if movement_type:
        query = query.filter_by(movement_type=movement_type)

    # Match the user's fitness level
    if difficulty:
        query = query.filter_by(difficulty=difficulty)

    activities = query.all()

    # Remove activities that require equipment the user doesn't have
    if equipment and equipment.lower() == "none":
        activities = [
            activity for activity in activities
            if not activity.equipment_required
            or activity.equipment_required.lower() == "none"
        ]

    # Prefer activities that fit within the user's available time
    if available_time:
        activities = [
            activity for activity in activities
            if activity.duration <= available_time
        ]

    return jsonify([
        {
            "id": activity.id,
            "name": activity.name,
            "category": activity.category,
            "duration": activity.duration,
            "difficulty": activity.difficulty,
            "movement_type": activity.movement_type,
            "equipment_required": activity.equipment_required,
            "instructions": activity.instructions
        }
        for activity in activities
    ])