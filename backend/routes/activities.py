from flask import Blueprint, jsonify
from models import Activity

activities_bp = Blueprint("activities", __name__)


@activities_bp.route("/api/activities", methods=["GET"])
def get_activities():
    activities = Activity.query.all()

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