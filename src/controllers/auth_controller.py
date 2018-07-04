from src import app, db

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from src.models.user import User

from src.helpers.auth_helper import required_roles


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    pass
