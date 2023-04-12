# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(80))
    poster = db.Column(db.String(80), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def __repr__(self):
        return f"Movie(title='{self.title}', description='{self.description}', poster='{self.poster}', created_at='{self.created_at}')"