from http import HTTPStatus
from flask import jsonify, request, current_app
from app.models.vaccination_models import VaccinationModel
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import Query
from app.configs.database import db
from psycopg2.errors import UniqueViolation


def create_vaccine_card():
    data = request.get_json()
    try:
        VaccinationModel.validate_keys(data)

        serialized_data = VaccinationModel.serialize(data)

        vaccine_card = VaccinationModel(**serialized_data)

        current_app.db.session.add(vaccine_card)
        current_app.db.session.commit()

        return jsonify(vaccine_card), HTTPStatus.CREATED

    except IntegrityError as e:
        if type(e.orig) == UniqueViolation:
            return {"error": "cpf already registered"}, HTTPStatus.CONFLICT
    except AttributeError:
        return {"error": "one or more of the inserted values are not strings"}, HTTPStatus.BAD_REQUEST
    except KeyError as e:
        return e.args[0], HTTPStatus.BAD_REQUEST
    except DataError:
        return {"error": "cpf value too long"}, HTTPStatus.BAD_REQUEST


def all_vaccine_cards():
    base_query: Query = db.session.query(VaccinationModel)

    vaccine_cards = base_query.order_by(VaccinationModel.first_shot_date).all()

    return jsonify(vaccine_cards), HTTPStatus.OK
