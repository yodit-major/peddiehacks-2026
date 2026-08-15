const getStartedBtn = document.getElementById("getStartedBtn");

const welcomeScreen = document.getElementById("welcomeScreen");
const profileScreen = document.getElementById("profileScreen");

const profileForm = document.getElementById("profileForm");


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

    const age = Number(document.getElementById("age").value);
    const difficulty = document.getElementById("difficulty").value;
    const goal = document.getElementById("goal").value;
    const movementType = document.getElementById("movementType").value;
    const availableTime = Number(document.getElementById("availableTime").value);
    const equipment = document.getElementById("equipment").value;


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

        console.log("Backend response:", data);


        if (!response.ok) {

            alert(
                data.error || "Something went wrong."
            );

            return;
        }


        alert(
            "Profile created successfully! 🎉"
        );


        console.log("User ID:", data.user_id);


    } catch (error) {

        console.error("Connection error:", error);

        alert(
            "Could not connect to Scroll2Sport backend."
        );

    }

});