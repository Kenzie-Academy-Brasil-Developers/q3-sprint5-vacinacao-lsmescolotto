from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    from app.models.vaccination_models import VaccinationModel

    Migrate(app=app, db=app.db, compare_type=True)