from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    fitness_level = db.Column(db.String(50), nullable=False)
    goal = db.Column(db.String(100), nullable=False)
    available_time = db.Column(db.Integer, nullable=False)
    movement_type = db.Column(db.String(50), nullable=False)
    equipment = db.Column(db.String(100), nullable=True)

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(30), nullable=False)
    movement_type = db.Column(db.String(50), nullable=False)
    equipment_required = db.Column(db.String(100), nullable=True)
    instructions = db.Column(db.Text, nullable=False)