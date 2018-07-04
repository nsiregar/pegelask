from src import app, db

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user, login_required, login_user, logout_user

from src.helpers.auth_helper import required_roles



home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
@home.route("/index", methods=["GET"])
def index():
    return render_template("/application/home.html", title="Home")
