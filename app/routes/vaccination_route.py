from flask import Blueprint
from app.controllers.vaccination_controller import create_vaccine_card, all_vaccine_cards


bp_vaccination = Blueprint("bp_vaccination", __name__, url_prefix="/vaccinations")

bp_vaccination.post("")(create_vaccine_card)
bp_vaccination.get("")(all_vaccine_cards)