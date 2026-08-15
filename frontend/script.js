const getStartedBtn = document.getElementById("getStartedBtn");

const welcomeScreen = document.getElementById("welcomeScreen");
const profileScreen = document.getElementById("profileScreen");
const recommendationScreen = document.getElementById("recommendationScreen");

const profileForm = document.getElementById("profileForm");

const recommendationTitle = document.getElementById("recommendationTitle");
const recommendationDuration = document.getElementById("recommendationDuration");
const recommendationDifficulty = document.getElementById("recommendationDifficulty");
const recommendationType = document.getElementById("recommendationType");
const recommendationDescription = document.getElementById("recommendationDescription");

const startWorkoutBtn = document.getElementById("startWorkoutBtn");
const workoutScreen = document.getElementById("workoutScreen");

const workoutTitle = document.getElementById("workoutTitle");

const workoutInstructions =
    document.getElementById("workoutInstructions");

const timerElement =
    document.getElementById("timer");

const completeWorkoutBtn =
    document.getElementById("completeWorkoutBtn");
let timerInterval = null;
let elapsedSeconds = 0;
let currentUserId = null;
let currentActivityId = null;
let currentActivityDuration = 0;
/* -----------------------------
   GO TO PROFILE
----------------------------- */

getStartedBtn.addEventListener("click", function () {

    welcomeScreen.classList.remove("active");

    profileScreen.classList.add("active");

});


/* -----------------------------
   SUBMIT PROFILE
----------------------------- */

profileForm.addEventListener("submit", async function (event) {

    event.preventDefault();


    const age = Number(
        document.getElementById("age").value
    );

    const difficulty =
        document.getElementById("difficulty").value;

    const goal =
        document.getElementById("goal").value;

    const movementType =
        document.getElementById("movementType").value;

    const availableTime = Number(
        document.getElementById("availableTime").value
    );

    const equipment =
        document.getElementById("equipment").value;


    const profileData = {

        age: age,

        fitness_level: difficulty,

        goal: goal,

        movement_type: movementType,

        available_time: availableTime,

        equipment: equipment

    };


    try {

        const response = await fetch(
            "http://127.0.0.1:5000/api/profile",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(profileData)
            }
        );


        const data = await response.json();


        console.log(
            "Backend response:",
            data
        );


        if (!response.ok) {

            alert(
                data.error ||
                "Something went wrong."
            );

            return;
        }


        console.log(
            "Profile created:",
            data
        );


        currentUserId = data.user_id;

        await loadRecommendation(currentUserId);


    } catch (error) {

        console.error(
            "Connection error:",
            error
        );

        alert(
            "Could not connect to Scroll2Sport backend."
        );

    }

});


/* -----------------------------
   LOAD RECOMMENDATION
----------------------------- */

async function loadRecommendation(userId) {

    try {

        const response = await fetch(
            `http://127.0.0.1:5000/api/recommendations?user_id=${userId}`
        );


        const data = await response.json();


        console.log(
            "Recommendation response:",
            data
        );


        if (!response.ok) {

            alert(
                data.error ||
                "Could not find a recommendation."
            );

            return;
        }


        const activity = Array.isArray(data)
            ? data[0]
            : data;
        currentActivityId = activity.id;

        currentActivityDuration =
        Number(activity.duration) || 0;

        if (!activity) {

            alert(
                "No suitable movement was found."
            );

            return;
        }


        recommendationTitle.textContent =
            activity.name ||
            "Your Movement Break";


        recommendationDuration.textContent =
            activity.duration
                ? `${activity.duration} minutes`
                : "Flexible";


        recommendationDifficulty.textContent =
            activity.difficulty ||
            "Beginner";


        recommendationType.textContent =
            activity.movement_type ||
            "Movement";


        recommendationDescription.textContent =
            activity.instructions ||
            "A movement break selected for your profile.";


        profileScreen.classList.remove(
            "active"
        );


        recommendationScreen.classList.add(
            "active"
        );


    } catch (error) {

        console.error(
            "Recommendation error:",
            error
        );


        alert(
            "Could not load your personalized movement."
        );

    }

}
/* -----------------------------
   START WORKOUT
----------------------------- */

startWorkoutBtn.addEventListener("click", function () {

    const title =
        recommendationTitle.textContent;

    const instructions =
        recommendationDescription.textContent;


    workoutTitle.textContent = title;

    workoutInstructions.textContent =
        instructions;


    recommendationScreen.classList.remove(
        "active"
    );

    workoutScreen.classList.add(
        "active"
    );


    startTimer();

});
/* -----------------------------
   TIMER
----------------------------- */

function startTimer() {

    elapsedSeconds = 0;

    updateTimer();


    timerInterval = setInterval(function () {

        elapsedSeconds++;

        updateTimer();

    }, 1000);

}


function updateTimer() {

    const minutes =
        Math.floor(elapsedSeconds / 60);

    const seconds =
        elapsedSeconds % 60;


    timerElement.textContent =
        `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;

}
/* -----------------------------
   COMPLETE WORKOUT
----------------------------- */

completeWorkoutBtn.addEventListener(
    "click",
    async function () {

        clearInterval(timerInterval);

        try {

            const response = await fetch(
                "http://127.0.0.1:5000/api/workouts",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        user_id: currentUserId,
                        activity_id: currentActivityId,
                        duration: currentActivityDuration
                    })
                }
            );


            const data = await response.json();


            console.log(
                "Workout completion response:",
                data
            );


            if (!response.ok) {

                alert(
                    data.error ||
                    "Could not save workout."
                );

                return;
            }


            alert(
                "Workout completed successfully! 🎉"
            );


        } catch (error) {

            console.error(
                "Workout completion error:",
                error
            );


            alert(
                "Could not connect to Scroll2Sport backend."
            );

        }

    }
);