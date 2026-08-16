from flask import Blueprint, request, jsonify
from models import User, Activity

recommendations_bp = Blueprint("recommendations", __name__)


@recommendations_bp.route("/api/recommendations", methods=["GET"])
def get_recommendations():

    user_id = request.args.get("user_id", type=int)

    if not user_id:
        return jsonify({
            "error": "User ID is required"
        }), 400


    # Find the user

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404


    # User preferences

    preferred_movement = user.movement_type
    preferred_difficulty = user.fitness_level
    available_time = user.available_time
    user_equipment = user.equipment or "None"


    # Get all activities that fit within the user's time

    activities = Activity.query.filter(
        Activity.duration <= available_time
    ).all()


    if not activities:

        return jsonify({
            "error": "No activity fits within your available time."
        }), 404


    # ---------------------------------------------------------
    # FILTER EQUIPMENT
    # ---------------------------------------------------------

    compatible_activities = []

    for activity in activities:

        required = activity.equipment_required or "None"

        # No equipment required = always okay

        if required.lower() == "none":
            compatible_activities.append(activity)
            continue


        # User has no equipment

        if user_equipment.lower() == "none":
            continue


        # User has the required equipment

        if required.lower() == user_equipment.lower():
            compatible_activities.append(activity)


    # If equipment filtering removed everything,
    # use activities requiring no equipment.

    if not compatible_activities:

        compatible_activities = [
            activity
            for activity in activities
            if not activity.equipment_required
            or activity.equipment_required.lower() == "none"
        ]


    # ---------------------------------------------------------
    # SCORE ACTIVITIES
    # ---------------------------------------------------------

    def score_activity(activity):

        score = 0


        # Exact movement type

        if activity.movement_type == preferred_movement:
            score += 50


        # Exact fitness level

        if activity.difficulty == preferred_difficulty:
            score += 40


        # Equipment match

        required = activity.equipment_required or "None"

        if required.lower() == "none":
            score += 10

        elif required.lower() == user_equipment.lower():
            score += 15


        # Prefer the longest activity that fits
        # Example: user chooses 10 minutes,
        # prefer 10 over 5 over 3.

        score += activity.duration


        return score


    # Sort from best match to worst match

    compatible_activities.sort(
        key=score_activity,
        reverse=True
    )


    # ---------------------------------------------------------
    # RETURN BEST MATCH
    # ---------------------------------------------------------

    if not compatible_activities:

        return jsonify({
            "error": "No suitable movement was found."
        }), 404


    best_activity = compatible_activities[0]


    return jsonify({

        "id": best_activity.id,

        "name": best_activity.name,

        "category": best_activity.category,

        "duration": best_activity.duration,

        "difficulty": best_activity.difficulty,

        "movement_type": best_activity.movement_type,

        "equipment_required":
            best_activity.equipment_required,

        "instructions":
            best_activity.instructions

    })