from src import app
from src import db
from datetime import datetime
from src.models.flags import Flag


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    messages = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    edited_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    votes = db.relationship("QuestionVote", backref="question", lazy="dynamic")

    def __repr__(self):
        return "Question {}".format(self.title)


class QuestionVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class QuestionFlag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    flag = db.Column(db.Enum(Flag))
