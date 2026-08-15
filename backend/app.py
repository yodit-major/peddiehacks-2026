from flask import Flask
from models import db
from routes.profile import profile_bp
from routes.activities import activities_bp
from recommendations import recommendations_bp
from workouts import workouts_bp
from progress import progress_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scroll2sport.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(profile_bp)
app.register_blueprint(activities_bp)
app.register_blueprint(recommendations_bp)
app.register_blueprint(workouts_bp)
app.register_blueprint(progress_bp)

@app.route("/")
def home():
    return "Scroll2Sport Backend is running! 🏃"


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)