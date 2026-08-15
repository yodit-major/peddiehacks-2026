from flask import Blueprint, jsonify
from models import WorkoutSession

progress_bp = Blueprint("progress", __name__)


@progress_bp.route("/api/progress/<int:user_id>", methods=["GET"])
def get_progress(user_id):

    workouts = WorkoutSession.query.filter_by(
        user_id=user_id,
        completed=True
    ).all()

    total_workouts = len(workouts)

    total_minutes = sum(
        workout.duration for workout in workouts
    )

    return jsonify({
        "user_id": user_id,
        "total_workouts": total_workouts,
        "total_minutes": total_minutes
    })