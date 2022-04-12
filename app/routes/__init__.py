from flask import Flask
from app.routes.vaccination_route import bp_vaccination


def init_app(app: Flask):
    app.register_blueprint(bp_vaccination)
