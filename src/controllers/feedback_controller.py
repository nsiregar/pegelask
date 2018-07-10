from src import app, db
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required
from src.models.question import Question, QuestionFlag, QuestionVote
from src.models.answer import Answer, AnswerFlag, AnswerVote
from src.models.comment import Comment, CommentFlag

feedback = Blueprint("feedback", __name__)

@feedback.route("/feedback/<int:id>", methods=["GET"])
def view(id):
    question = Question.query.filter_by(id=id).first()
    return render_template("/feedback/detail.html", title="Feedback", question=question)
