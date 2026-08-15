from flask import Blueprint, request, jsonify
from models import db, WorkoutSession

workouts_bp = Blueprint("workouts", __name__)


@workouts_bp.route("/api/workouts", methods=["POST"])
def complete_workout():

    data = request.get_json()

    user_id = data.get("user_id")
    activity_id = data.get("activity_id")
    duration = data.get("duration")

    if not user_id or not activity_id or not duration:
        return jsonify({
            "error": "user_id, activity_id and duration are required"
        }), 400

    session = WorkoutSession(
        user_id=user_id,
        activity_id=activity_id,
        duration=duration,
        completed=True
    )

    db.session.add(session)
    db.session.commit()

    return jsonify({
        "message": "Workout completed successfully!",
        "workout_id": session.id
    }), 201