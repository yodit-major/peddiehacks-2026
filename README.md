\# 🏃 Scroll2Sport





\### Scroll less. Move more.





Scroll2Sport is an inclusive sports and movement web application designed to help people turn long periods of screen use into opportunities for physical activity.





Instead of simply telling users to stop scrolling, Scroll2Sport encourages them to take movement breaks and provides personalized activities based on their profile, fitness level, goals, available time, movement preference, and equipment.





\---





\## 🎯 PeddieHacks 2026





\*\*Track:\*\* Sports  

\*\*Hackathon:\*\* PeddieHacks 2026  

\*\*Project:\*\* Scroll2Sport











\## 💡 The Problem





People spend long periods of time scrolling and using screens, which can lead to extended periods of inactivity.





At the same time, exercise recommendations are often not personalized. A workout that works for one person may not work for someone with a different fitness level, mobility need, amount of available time, or physical ability.





We wanted to create a simple and inclusive way to encourage people to move more.











\## 🏃 Our Solution





Scroll2Sport turns screen time into a reason to move.





Users create a profile and receive movement recommendations based on their individual needs.





The application allows users to:





\- Create an account

\- Log in securely

\- Create a personalized movement profile

\- Start a scrolling session

\- Receive a reminder when it is time to move

\- Skip scrolling and start moving immediately

\- Receive a personalized movement recommendation

\- Complete a timed workout

\- Track completed workouts

\- View total workouts and total minutes moved

\- View recent workout history











\## ♿ Inclusive Movement





Movement should be accessible to everyone.





Scroll2Sport allows users to choose a movement type that fits their needs:





\- 🧍 Standing

\- 🪑 Seated

\- 💚 Low Impact





This helps make movement recommendations more inclusive for people with different mobility needs and physical abilities.





Our goal is not to force everyone into the same workout, but to help users find movement that works for them.











\## ✨ Main Features

🏗️ Architecture



Scroll2Sport uses a frontend-backend architecture.



&#x20;               ┌──────────────────────┐

&#x20;               │      Frontend        │

&#x20;               │                      │

&#x20;               │    HTML / CSS / JS   │

&#x20;               └──────────┬───────────┘

&#x20;                          │

&#x20;                          │ REST API

&#x20;                          │

&#x20;               ┌──────────▼───────────┐

&#x20;               │       Backend        │

&#x20;               │                      │

&#x20;               │        Flask         │

&#x20;               │   Flask-SQLAlchemy   │

&#x20;               │      Flask-CORS      │

&#x20;               └──────────┬───────────┘

&#x20;                          │

&#x20;                          ▼

&#x20;                      Database



The frontend handles the user interface and interaction.



The Flask backend handles:



Authentication

User profiles

Movement recommendations

Workout records

Progress tracking

🛠️ Technologies

Frontend

HTML5

CSS3

JavaScript

Backend

Python

Flask

Flask-SQLAlchemy

Flask-CORS

Database

SQLite

📁 Project Structure

peddiehacks-2026/

│

├── backend/

│   ├── app.py

│   ├── auth.py

│   ├── models.py

│   ├── progress.py

│   ├── recommendations.py

│   ├── seed.py

│   │

│   └── routes/

│       └── profile.py

│

├── frontend/

│   ├── index.html

│   ├── script.js

│   └── style.css

│

├── requirements.txt

├── .gitignore

└── README.md

🚀 How to Run

1\. Clone the repository

git clone https://github.com/yodit-major/peddiehacks-2026.git

2\. Enter the project

cd peddiehacks-2026

3\. Create a virtual environment

python -m venv venv

4\. Activate the virtual environment



On Windows PowerShell:



.\\venv\\Scripts\\Activate.ps1

5\. Install dependencies

pip install -r requirements.txt

6\. Start the Flask backend

cd backend

python app.py



The Flask server runs locally at:



http://127.0.0.1:5000

7\. Open the frontend



Open:



frontend/index.html



in a web browser.



Make sure the Flask backend is running while using the application.



🌍 Impact



Scroll2Sport is designed to address a simple problem:



People spend too much time sitting and scrolling, and not enough time moving.



Instead of treating technology as the enemy, Scroll2Sport uses screen time as an opportunity to encourage physical activity.



A short movement break can be easier to start than a full workout.



Our goal is to make movement:



Simple

Personalized

Inclusive

Time-efficient

Fun

👥 Intended Users



Scroll2Sport is designed for people who:



Spend long periods using screens

Want simple movement breaks

Have different fitness levels

Have limited time for exercise

Prefer seated or low-impact movement

Want to track their physical activity

Need movement options that better fit their physical abilities

🎯 Why Sports?



Sports and physical activity do not have to mean intense workouts.



Scroll2Sport focuses on making movement a regular part of someone's day.



Whether someone has three minutes, five minutes, or ten minutes, there is an opportunity to move.



Small movements can become healthy habits.



🔮 Future Improvements



If we continue developing Scroll2Sport beyond the hackathon, we would like to add:



More movement and sports activities

More accessibility options

Smarter recommendation algorithms

Daily and weekly movement goals

Activity streaks

Achievements and rewards

More detailed progress analytics

Mobile application support

Integration with device screen-time data

More personalized activity plans

🏆 Hackathon



Scroll2Sport was created specifically for PeddieHacks 2026 under the Sports Track.



The project was developed during the hackathon with the goal of creating a practical, inclusive, and accessible approach to physical activity.



🏃 Scroll less. Move more.

Movement for everyone. ♿

