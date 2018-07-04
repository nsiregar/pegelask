from src import app
from src import db
from src.controllers.auth_controller import auth
from src.controllers.home_controller import home

app.register_blueprint(auth)
app.register_blueprint(home)
