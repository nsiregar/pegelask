import jwt
from src import app
from src import db
from src import login
from time import time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from src.models.answer import Answer
from src.models.answer import AnswerVote
from src.models.answer import AnswerFlag
from src.models.comment import Comment
from src.models.comment import CommentFlag
from src.models.question import Question
from src.models.question import QuestionVote
from src.models.question import QuestionFlag


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(255))
    answers = db.relationship("Answer", backref="user", lazy="dynamic")
    answer_votes = db.relationship("AnswerVote", backref="user", lazy="dynamic")
    answer_flags = db.relationship("AnswerFlag", backref="user", lazy="dynamic")
    comments = db.relationship("Comment", backref="user", lazy="dynamic")
    comment_flags = db.relationship("CommentFlag", backref="user", lazy="dynamic")
    questions = db.relationship("Question", backref="user", lazy="dynamic")
    question_votes = db.relationship("QuestionVote", backref="user", lazy="dynamic")
    question_flags = db.relationship("QuestionFlag", backref="user", lazy="dynamic")

    @staticmethod
    def verify_token(token):
        id = jwt.decode(token, app.config.get("SECRET_KEY"), algorithms=["HS256"])[
            "reset_password"
        ]
        return User.query.get(id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_token(self, expires=600):
        token = jwt.encode(
            {"reset_password": self.id, "exp": time() + expires},
            app.config.get("SECRET_KEY"),
            algorithm="HS256",
        ).decode("utf-8")
        return token

    def __repr__(self):
        return "User {}".format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
