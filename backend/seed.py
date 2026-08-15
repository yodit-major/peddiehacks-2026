from app import app
from models import db, Activity


activities = [
    {
        "name": "Seated Arm Circles",
        "category": "Mobility",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "None",
        "instructions": "Sit upright and slowly make circles with both arms."
    },
    {
        "name": "Seated Punches",
        "category": "Cardio",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "None",
        "instructions": "Sit upright and alternate punching forward at a comfortable pace."
    },
    {
        "name": "Seated Knee Lifts",
        "category": "Cardio",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "None",
        "instructions": "Sit upright and gently lift one knee at a time."
    },
    {
        "name": "Shoulder Rolls",
        "category": "Mobility",
        "duration": 2,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "None",
        "instructions": "Slowly roll your shoulders forward and backward."
    },
    {
        "name": "Ankle Circles",
        "category": "Mobility",
        "duration": 2,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "None",
        "instructions": "Lift one foot slightly and slowly rotate your ankle."
    },
    {
        "name": "Gentle Marching",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Stand safely and march gently in place."
    },
    {
        "name": "Step Touch",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Step gently from side to side at a comfortable pace."
    },
    {
        "name": "Wall Push-Ups",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "Wall",
        "instructions": "Place your hands against a wall and perform controlled push-ups."
    },
    {
        "name": "Bodyweight Squats",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Lower your body into a comfortable squat and return to standing."
    },
    {
        "name": "Standing Side Steps",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Take controlled steps from side to side."
    },
    {
        "name": "Seated Leg Extensions",
        "category": "Strength",
        "duration": 4,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and slowly extend one leg at a time."
    },
    {
        "name": "Seated Torso Rotation",
        "category": "Mobility",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and gently rotate your torso from side to side."
    }
]


with app.app_context():
    for activity_data in activities:
        activity = Activity(**activity_data)
        db.session.add(activity)

    db.session.commit()

    print(f"Added {len(activities)} activities successfully!")