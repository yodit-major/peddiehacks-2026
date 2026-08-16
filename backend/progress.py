from flask import Blueprint, jsonify
from models import WorkoutSession, Activity

progress_bp = Blueprint("progress", __name__)


@progress_bp.route("/api/progress/<int:user_id>", methods=["GET"])
def get_progress(user_id):

    workouts = WorkoutSession.query.filter_by(
        user_id=user_id,
        completed=True
    ).order_by(
        WorkoutSession.created_at.desc()
    ).all()

    total_workouts = len(workouts)

    total_minutes = sum(
        workout.duration
        for workout in workouts
    )

    workout_history = []

    for workout in workouts:

        activity = Activity.query.get(
            workout.activity_id
        )

        workout_history.append({
            "workout_id": workout.id,
            "activity_id": workout.activity_id,
            "activity_name": (
                activity.name
                if activity
                else "Workout"
            ),
            "duration": workout.duration,
            "completed_at": (
                workout.created_at.isoformat()
                if workout.created_at
                else None
            )
        })

    return jsonify({

        "user_id": user_id,

        "total_workouts": total_workouts,

        "total_minutes": total_minutes,

        "workout_history": workout_history

    })