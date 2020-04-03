from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default_profile_pic.jpg')
    team_image_file = db.Column(db.String(20),nullable=False, default='no_team_selected.jpg')
    password = db.Column(db.String(60), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    # matches = db.relationship('Matches', backref='creator', lazy=True)

    def __repr__(Self):
        return f"User('{Self.username}', '{Self.email}', '{Self.image_file}')"


#### TODO Class(es) of matches ####
class Matches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matches = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(Self):
        return f"Matches('{Self.matches}', {Self.user_id})"
###################################


