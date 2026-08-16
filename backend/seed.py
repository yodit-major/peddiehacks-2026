from app import app
from models import db, Activity


activities = [

    # =========================================================
    # BEGINNER - STANDING
    # =========================================================

    {
        "name": "Gentle Standing March",
        "category": "Cardio",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Stand tall and gently march in place. Keep your movements comfortable and swing your arms naturally."
    },

    {
        "name": "Standing Shoulder Rolls",
        "category": "Mobility",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Stand comfortably. Slowly roll your shoulders backward in a smooth circular motion, then reverse the direction."
    },

    {
        "name": "Standing Side Steps",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Take small steps from side to side. Keep your knees slightly bent and maintain a comfortable pace."
    },

    {
        "name": "Standing Reach and Stretch",
        "category": "Mobility",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Reach both arms overhead, gently stretch upward, then lower your arms. Repeat slowly while breathing comfortably."
    },


    # =========================================================
    # BEGINNER - SEATED
    # =========================================================

    {
        "name": "Seated Knee Lifts",
        "category": "Mobility",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright in a stable chair. Lift one knee at a time toward your chest and lower it slowly."
    },

    {
        "name": "Seated Ankle Circles",
        "category": "Mobility",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and extend one foot slightly forward. Slowly make circles with your ankle, then switch sides."
    },

    {
        "name": "Seated Arm Raises",
        "category": "Mobility",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit tall with your feet on the floor. Raise your arms forward or overhead as comfortably as possible, then lower them."
    },

    {
        "name": "Seated Marching",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and alternate lifting your knees as if marching. Keep your movements controlled."
    },


    # =========================================================
    # BEGINNER - LOW IMPACT
    # =========================================================

    {
        "name": "Gentle Toe Taps",
        "category": "Cardio",
        "duration": 3,
        "difficulty": "Beginner",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Stand comfortably and alternate tapping your toes forward. Keep the movement light and controlled."
    },

    {
        "name": "Low Impact Side Reach",
        "category": "Mobility",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Step gently to one side while reaching your arms outward. Return to the center and repeat on the other side."
    },

    {
        "name": "Gentle Step Touch",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Beginner",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Step to one side and bring the other foot toward it. Alternate sides at a comfortable pace."
    },

    {
        "name": "Easy Full Body Stretch",
        "category": "Mobility",
        "duration": 10,
        "difficulty": "Beginner",
        "movement_type": "Low Impact",
        "equipment_required": "Mat",
        "instructions": "Perform gentle full-body stretches at a comfortable pace. Avoid bouncing and stop if you feel pain."
    },


    # =========================================================
    # INTERMEDIATE - STANDING
    # =========================================================

    {
        "name": "Standing Knee Drives",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Stand tall and drive one knee upward at a time. Alternate legs while keeping your core engaged."
    },

    {
        "name": "Bodyweight Squats",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Stand with your feet about shoulder-width apart. Bend your knees and hips into a comfortable squat, then stand back up."
    },

    {
        "name": "Standing Reverse Lunges",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Step one foot backward and lower your body under control. Return to standing and alternate legs."
    },

    {
        "name": "Standing Dynamic Stretch",
        "category": "Mobility",
        "duration": 10,
        "difficulty": "Intermediate",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Perform controlled leg swings, arm circles, torso rotations, and gentle dynamic stretches."
    },


    # =========================================================
    # INTERMEDIATE - SEATED
    # =========================================================

    {
        "name": "Seated Leg Extensions",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and extend one leg until it is comfortably straight. Lower it slowly and alternate legs."
    },

    {
        "name": "Seated Torso Rotations",
        "category": "Mobility",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit tall with your feet grounded. Rotate your torso gently from side to side while keeping the movement controlled."
    },

    {
        "name": "Seated Knee-to-Chest",
        "category": "Mobility",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and bring one knee toward your chest using controlled movement. Alternate sides."
    },

    {
        "name": "Seated Upper Body Workout",
        "category": "Strength",
        "duration": 10,
        "difficulty": "Intermediate",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Perform controlled seated arm raises, punches, shoulder presses, and torso movements."
    },


    # =========================================================
    # INTERMEDIATE - LOW IMPACT
    # =========================================================

    {
        "name": "Low Impact Squat and Reach",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Perform a comfortable shallow squat and reach your arms overhead as you stand."
    },

    {
        "name": "Low Impact Knee Lifts",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Intermediate",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Alternate controlled knee lifts while keeping the movement smooth and low impact."
    },

    {
        "name": "Low Impact Cardio Flow",
        "category": "Cardio",
        "duration": 10,
        "difficulty": "Intermediate",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Combine step touches, knee lifts, gentle reaches, and controlled side steps into a continuous low-impact routine."
    },


    # =========================================================
    # ADVANCED - STANDING
    # =========================================================

    {
        "name": "Fast High Knees",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Advanced",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Stand tall and alternate driving your knees upward at a faster pace while maintaining control."
    },

    {
        "name": "Advanced Bodyweight Squats",
        "category": "Strength",
        "duration": 5,
        "difficulty": "Advanced",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Perform controlled bodyweight squats at a challenging but manageable pace. Maintain good posture throughout."
    },

    {
        "name": "Reverse Lunge and Knee Drive",
        "category": "Strength",
        "duration": 10,
        "difficulty": "Advanced",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Step backward into a reverse lunge and drive the back knee forward as you return to standing. Alternate sides."
    },

    {
        "name": "Standing Cardio Circuit",
        "category": "Cardio",
        "duration": 10,
        "difficulty": "Advanced",
        "movement_type": "Standing",
        "equipment_required": "None",
        "instructions": "Combine high knees, side steps, squats, and controlled jumping-free cardio movements."
    },


    # =========================================================
    # ADVANCED - SEATED
    # =========================================================

    {
        "name": "Advanced Seated Knee Drives",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Advanced",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit upright and alternate driving your knees upward at a controlled but challenging pace."
    },

    {
        "name": "Seated Power Punches",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Advanced",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Sit tall and perform alternating controlled punches at a steady pace while keeping your core engaged."
    },

    {
        "name": "Advanced Seated Cardio",
        "category": "Cardio",
        "duration": 10,
        "difficulty": "Advanced",
        "movement_type": "Seated",
        "equipment_required": "Chair",
        "instructions": "Combine seated knee drives, alternating punches, arm movements, and controlled torso movements."
    },


    # =========================================================
    # ADVANCED - LOW IMPACT
    # =========================================================

    {
        "name": "Low Impact Power Steps",
        "category": "Cardio",
        "duration": 5,
        "difficulty": "Advanced",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Perform fast but controlled side steps, knee lifts, and reaches without jumping."
    },

    {
        "name": "Low Impact Strength Flow",
        "category": "Strength",
        "duration": 10,
        "difficulty": "Advanced",
        "movement_type": "Low Impact",
        "equipment_required": "Mat",
        "instructions": "Combine controlled squats, lunges, glute bridges, and core movements at a challenging but manageable pace."
    },

    {
        "name": "Advanced Low Impact Cardio",
        "category": "Cardio",
        "duration": 10,
        "difficulty": "Advanced",
        "movement_type": "Low Impact",
        "equipment_required": "None",
        "instructions": "Perform a continuous sequence of fast step touches, knee lifts, side steps, and upper-body movements without jumping."
    }
]


with app.app_context():

    db.create_all()

    # Remove existing activities before reseeding
    Activity.query.delete()

    for activity_data in activities:

        activity = Activity(
            name=activity_data["name"],
            category=activity_data["category"],
            duration=activity_data["duration"],
            difficulty=activity_data["difficulty"],
            movement_type=activity_data["movement_type"],
            equipment_required=activity_data["equipment_required"],
            instructions=activity_data["instructions"]
        )

        db.session.add(activity)

    db.session.commit()

    print(
        f"Successfully seeded {len(activities)} activities! 🎉"
    )