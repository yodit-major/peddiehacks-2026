/* =========================================================
   SCROLL2SPORT - MAIN JAVASCRIPT
========================================================= */


/* =========================================================
   ELEMENTS
========================================================= */

const getStartedBtn = document.getElementById("getStartedBtn");
const loginBtn = document.getElementById("loginBtn");

const welcomeScreen = document.getElementById("welcomeScreen");
const authScreen = document.getElementById("authScreen");
const profileScreen = document.getElementById("profileScreen");
const scrollBreakScreen = document.getElementById("scrollBreakScreen");
const recommendationScreen = document.getElementById("recommendationScreen");
const workoutScreen = document.getElementById("workoutScreen");
const progressScreen = document.getElementById("progressScreen");

const profileForm = document.getElementById("profileForm");
const registerForm = document.getElementById("registerForm");
const loginForm = document.getElementById("loginForm");

const switchAuthBtn = document.getElementById("switchAuthBtn");
const authSwitchText = document.getElementById("authSwitchText");
const authTitle = document.getElementById("authTitle");
const authDescription = document.getElementById("authDescription");


/* -----------------------------
   SCROLL
----------------------------- */

const startScrollBtn =
    document.getElementById("startScrollBtn");

const stopScrollBtn =
    document.getElementById("stopScrollBtn");

const startMovementNowBtn =
    document.getElementById("startMovementNowBtn");

const scrollTimer =
    document.getElementById("scrollTimer");

const scrollStatus =
    document.getElementById("scrollStatus");


/* -----------------------------
   RECOMMENDATION
----------------------------- */

const recommendationTitle =
    document.getElementById("recommendationTitle");

const recommendationDuration =
    document.getElementById("recommendationDuration");

const recommendationDifficulty =
    document.getElementById("recommendationDifficulty");

const recommendationType =
    document.getElementById("recommendationType");

const recommendationDescription =
    document.getElementById("recommendationDescription");

const startWorkoutBtn =
    document.getElementById("startWorkoutBtn");


/* -----------------------------
   WORKOUT
----------------------------- */

const workoutTitle =
    document.getElementById("workoutTitle");

const workoutInstructions =
    document.getElementById("workoutInstructions");

const timerElement =
    document.getElementById("timer");

const completeWorkoutBtn =
    document.getElementById("completeWorkoutBtn");


/* -----------------------------
   PROGRESS
----------------------------- */

const totalWorkouts =
    document.getElementById("totalWorkouts");

const totalMinutes =
    document.getElementById("totalMinutes");

const workoutHistoryList =
    document.getElementById("workoutHistoryList");

const backHomeBtn =
    document.getElementById("backHomeBtn");


/* =========================================================
   VARIABLES
========================================================= */

let currentUserId = null;
let currentActivityId = null;

let scrollInterval = null;
let scrollElapsedSeconds = 0;

let workoutInterval = null;
let workoutElapsedSeconds = 0;


/*
   TESTING:

   30 seconds = reminder after 30 seconds.

   AFTER TESTING CHANGE TO:

   const SCROLL_REMINDER_SECONDS = 30 * 60;

   That means 30 minutes.
*/

const SCROLL_REMINDER_SECONDS = 30 * 60;


/* =========================================================
   SCREEN MANAGEMENT
========================================================= */

const screens = [
    welcomeScreen,
    authScreen,
    profileScreen,
    scrollBreakScreen,
    recommendationScreen,
    workoutScreen,
    progressScreen
];


function showScreen(screen) {

    screens.forEach(function (item) {

        item.classList.remove("active");

    });

    screen.classList.add("active");
}


/* =========================================================
   API HELPER
========================================================= */

async function apiRequest(
    url,
    options = {},
    defaultError = "Something went wrong."
) {

    const response = await fetch(url, options);

    let data = {};

    try {

        data = await response.json();

    } catch (error) {

        data = {};

    }


    if (!response.ok) {

        throw new Error(
            data.error || defaultError
        );

    }


    return data;
}


/* =========================================================
   BROWSER NOTIFICATIONS
========================================================= */

async function requestNotificationPermission() {

    if (!("Notification" in window)) {

        console.log(
            "Browser notifications are not supported."
        );

        return false;
    }


    if (Notification.permission === "granted") {

        return true;
    }


    if (Notification.permission === "default") {

        try {

            const permission =
                await Notification.requestPermission();

            return permission === "granted";

        } catch (error) {

            console.error(
                "Notification permission error:",
                error
            );

            return false;
        }
    }


    return false;
}


/* -----------------------------
   SHOW NOTIFICATION
----------------------------- */

function showScrollReminderNotification() {

    if (!("Notification" in window)) {
        return;
    }


    if (Notification.permission !== "granted") {
        return;
    }


    try {

        const notification =
            new Notification(
                "🏃 Scroll2Sport — Time to Move!",
                {
                    body:
                        "You've been scrolling for a while. Take a movement break! 💪",

                    tag:
                        "scroll2sport-reminder"
                }
            );


        notification.onclick =
            function () {

                window.focus();

                notification.close();

            };


    } catch (error) {

        console.error(
            "Notification error:",
            error
        );

    }
}


/* =========================================================
   AUTHENTICATION
========================================================= */


/* -----------------------------
   GET STARTED
----------------------------- */

getStartedBtn.addEventListener(
    "click",
    function () {

        showScreen(authScreen);

    }
);


/* -----------------------------
   LOGIN BUTTON
----------------------------- */

loginBtn.addEventListener(
    "click",
    function () {

        showScreen(authScreen);

        showLoginForm();

    }
);


/* -----------------------------
   REGISTER FORM
----------------------------- */

function showRegisterForm() {

    registerForm.style.display = "block";
    loginForm.style.display = "none";

    authTitle.textContent =
        "Create your account";

    authDescription.textContent =
        "Create an account to save your progress and personalized movements.";

    authSwitchText.textContent =
        "Already have an account?";

    switchAuthBtn.textContent =
        "Login";
}


/* -----------------------------
   LOGIN FORM
----------------------------- */

function showLoginForm() {

    registerForm.style.display = "none";
    loginForm.style.display = "block";

    authTitle.textContent =
        "Welcome back!";

    authDescription.textContent =
        "Login to continue your personalized movement journey.";

    authSwitchText.textContent =
        "Don't have an account?";

    switchAuthBtn.textContent =
        "Create Account";
}


/* -----------------------------
   SWITCH AUTH
----------------------------- */

switchAuthBtn.addEventListener(
    "click",
    function () {

        if (
            registerForm.style.display === "none"
        ) {

            showRegisterForm();

        } else {

            showLoginForm();

        }

    }
);


/* =========================================================
   REGISTER
========================================================= */

registerForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const username =
            document
                .getElementById("registerUsername")
                .value
                .trim();

        const password =
            document
                .getElementById("registerPassword")
                .value;


        try {

            const data =
                await apiRequest(
                    "http://127.0.0.1:5000/api/register",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            username: username,
                            password: password
                        })
                    },
                    "Could not create account."
                );


            currentUserId =
                data.user_id;


            localStorage.setItem(
                "scroll2sport_user_id",
                currentUserId
            );


            alert(
                "Account created successfully! 🎉"
            );


            showScreen(profileScreen);


        } catch (error) {

            console.error(
                "Registration error:",
                error
            );


            alert(
                error.message
            );

        }

    }
);


/* =========================================================
   LOGIN
========================================================= */

loginForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const username =
            document
                .getElementById("loginUsername")
                .value
                .trim();

        const password =
            document
                .getElementById("loginPassword")
                .value;


        try {

            const data =
                await apiRequest(
                    "http://127.0.0.1:5000/api/login",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            username: username,
                            password: password
                        })
                    },
                    "Login failed."
                );


            currentUserId =
                data.user_id;


            localStorage.setItem(
                "scroll2sport_user_id",
                currentUserId
            );


            alert(
                "Login successful! 🎉"
            );


            showScreen(profileScreen);


        } catch (error) {

            console.error(
                "Login error:",
                error
            );


            alert(
                error.message
            );

        }

    }
);


/* =========================================================
   PROFILE
========================================================= */

profileForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        const profileData = {

            user_id:
                currentUserId,

            age:
                Number(
                    document
                        .getElementById("age")
                        .value
                ),

            fitness_level:
                document
                    .getElementById("difficulty")
                    .value,

            goal:
                document
                    .getElementById("goal")
                    .value,

            movement_type:
                document
                    .getElementById("movementType")
                    .value,

            available_time:
                Number(
                    document
                        .getElementById("availableTime")
                        .value
                ),

            equipment:
                document
                    .getElementById("equipment")
                    .value
        };


        try {

            const data =
                await apiRequest(
                    "http://127.0.0.1:5000/api/profile",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(profileData)
                    },
                    "Could not save profile."
                );


            currentUserId =
                data.user_id;


            /*
               After profile:

               USER CAN CHOOSE:

               1. Start scrolling
               2. Start movement immediately
            */

            showScrollBreak();


        } catch (error) {

            console.error(
                "Profile error:",
                error
            );


            alert(
                error.message
            );

        }

    }
);


/* =========================================================
   SCROLL BREAK
========================================================= */


/* -----------------------------
   SHOW SCROLL BREAK SCREEN
----------------------------- */

function showScrollBreak() {

    clearInterval(scrollInterval);

    scrollElapsedSeconds = 0;

    updateScrollTimer();


    scrollStatus.textContent =
        "Want to scroll first? Start your session and we'll remind you when it's time to move.";


    startScrollBtn.style.display =
        "inline-block";


    stopScrollBtn.style.display =
        "none";


    /*
       IMPORTANT:

       This button lets the user skip
       scrolling completely.
    */

    startMovementNowBtn.style.display =
        "inline-block";


    showScreen(scrollBreakScreen);
}


/* =========================================================
   START SCROLLING
========================================================= */

startScrollBtn.addEventListener(
    "click",
    async function () {

        clearInterval(scrollInterval);

        scrollElapsedSeconds = 0;

        updateScrollTimer();


        /*
           Ask notification permission
           because this is a user click.
        */

        const notificationsAllowed =
            await requestNotificationPermission();


        if (notificationsAllowed) {

            scrollStatus.textContent =
                "You're scrolling... 🔔 We'll notify you when it's time to move.";

        } else {

            scrollStatus.textContent =
                "You're scrolling... We'll remind you when it's time to move.";

        }


        startScrollBtn.style.display =
            "none";


        startMovementNowBtn.style.display =
            "inline-block";


        stopScrollBtn.style.display =
            "none";


        scrollInterval =
            setInterval(
                function () {

                    scrollElapsedSeconds++;

                    updateScrollTimer();


                    if (
                        scrollElapsedSeconds >=
                        SCROLL_REMINDER_SECONDS
                    ) {

                        clearInterval(
                            scrollInterval
                        );


                        scrollStatus.textContent =
                            "⏰ Time to move! Your body deserves a break. 🏃";


                        stopScrollBtn.style.display =
                            "inline-block";


                        showScrollReminderNotification();

                    }

                },
                1000
            );

    }
);


/* =========================================================
   SCROLL TIMER
========================================================= */

function updateScrollTimer() {

    const minutes =
        Math.floor(
            scrollElapsedSeconds / 60
        );


    const seconds =
        scrollElapsedSeconds % 60;


    scrollTimer.textContent =
        `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}


/* =========================================================
   START MOVEMENT NOW
========================================================= */

/*
   This is the important new feature.

   The user DOES NOT have to scroll.

   They can immediately receive
   their personalized movement.
*/

startMovementNowBtn.addEventListener(
    "click",
    async function () {

        clearInterval(scrollInterval);


        scrollElapsedSeconds = 0;

        updateScrollTimer();


        scrollStatus.textContent =
            "Let's get you moving! 🏃";


        await loadRecommendation(
            currentUserId
        );

    }
);


/* =========================================================
   READY TO MOVE AFTER SCROLL
========================================================= */

stopScrollBtn.addEventListener(
    "click",
    async function () {

        clearInterval(scrollInterval);


        scrollStatus.textContent =
            "Great choice! Let's get you moving. 🏃";


        await loadRecommendation(
            currentUserId
        );

    }
);


/* =========================================================
   RECOMMENDATION
========================================================= */

async function loadRecommendation(userId) {

    try {

        const data =
            await apiRequest(
                `http://127.0.0.1:5000/api/recommendations?user_id=${userId}`,
                {},
                "Could not find a recommendation."
            );


        console.log(
            "Recommendation response:",
            data
        );


        const activity =
            Array.isArray(data)
                ? data[0]
                : data;


        if (!activity) {

            alert(
                "No suitable movement was found."
            );

            return;
        }


        currentActivityId =
            activity.id;


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


        showScreen(
            recommendationScreen
        );


    } catch (error) {

        console.error(
            "Recommendation error:",
            error
        );


        alert(
            error.message
        );

    }
}


/* =========================================================
   START WORKOUT
========================================================= */

startWorkoutBtn.addEventListener(
    "click",
    function () {

        workoutTitle.textContent =
            recommendationTitle.textContent;


        workoutInstructions.textContent =
            recommendationDescription.textContent;


        showScreen(
            workoutScreen
        );


        startWorkoutTimer();

    }
);


/* =========================================================
   WORKOUT TIMER
========================================================= */

function startWorkoutTimer() {

    clearInterval(workoutInterval);

    workoutElapsedSeconds = 0;

    updateWorkoutTimer();


    workoutInterval =
        setInterval(
            function () {

                workoutElapsedSeconds++;

                updateWorkoutTimer();

            },
            1000
        );
}


/* -----------------------------
   UPDATE WORKOUT TIMER
----------------------------- */

function updateWorkoutTimer() {

    const minutes =
        Math.floor(
            workoutElapsedSeconds / 60
        );


    const seconds =
        workoutElapsedSeconds % 60;


    timerElement.textContent =
        `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}


/* =========================================================
   COMPLETE WORKOUT
========================================================= */

completeWorkoutBtn.addEventListener(
    "click",
    async function () {

        clearInterval(workoutInterval);


        /*
           Convert seconds to minutes.

           Minimum = 1 minute.
        */

        const actualDuration =
            Math.max(
                1,
                Math.ceil(
                    workoutElapsedSeconds / 60
                )
            );


        try {

            const data =
                await apiRequest(
                    "http://127.0.0.1:5000/api/workouts",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({

                            user_id:
                                currentUserId,

                            activity_id:
                                currentActivityId,

                            duration:
                                actualDuration

                        })
                    },
                    "Could not save workout."
                );


            console.log(
                "Workout saved:",
                data
            );


            await loadProgress(
                currentUserId
            );


        } catch (error) {

            console.error(
                "Workout completion error:",
                error
            );


            alert(
                error.message
            );

        }

    }
);


/* =========================================================
   PROGRESS
========================================================= */

async function loadProgress(userId) {

    try {

        const data =
            await apiRequest(
                `http://127.0.0.1:5000/api/progress/${userId}`,
                {},
                "Could not load progress."
            );


        totalWorkouts.textContent =
            data.total_workouts;


        totalMinutes.textContent =
            data.total_minutes;


        workoutHistoryList.innerHTML =
            "";


        /*
           WORKOUT HISTORY
        */

        if (
            data.workout_history &&
            data.workout_history.length > 0
        ) {

            data.workout_history.forEach(
                function (workout) {

                    const workoutItem =
                        document.createElement("div");


                    workoutItem.classList.add(
                        "history-item"
                    );


                    const workoutName =
                        document.createElement("strong");


                    workoutName.textContent =
                        `🏃 ${workout.activity_name}`;


                    const workoutDuration =
                        document.createElement("span");


                    workoutDuration.textContent =
                        `${workout.duration} minutes`;


                    workoutItem.appendChild(
                        workoutName
                    );


                    workoutItem.appendChild(
                        workoutDuration
                    );


                    workoutHistoryList.appendChild(
                        workoutItem
                    );

                }
            );


        } else {

            const emptyMessage =
                document.createElement("p");


            emptyMessage.textContent =
                "No workouts yet.";


            workoutHistoryList.appendChild(
                emptyMessage
            );

        }


        showScreen(
            progressScreen
        );


    } catch (error) {

        console.error(
            "Progress error:",
            error
        );


        alert(
            error.message
        );

    }
}


/* =========================================================
   BACK HOME
========================================================= */

backHomeBtn.addEventListener(
    "click",
    function () {

        clearInterval(scrollInterval);

        clearInterval(workoutInterval);


        showScreen(
            welcomeScreen
        );

    }
);