from dataclasses import dataclass
from datetime import datetime, timedelta
from sqlalchemy import CheckConstraint, Column, DateTime, String 
from app.configs.database import db


@dataclass
class VaccinationModel(db.Model):

    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vaccine_name: str
    health_unit_name: str


    __tablename__ = "vaccine_cards"
    __table_args__ = (CheckConstraint("cpf ~ '\d{11}'"),)
    

    cpf = Column(String(11), primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime, default=datetime.now())
    second_shot_date = Column(DateTime, default=datetime.now() + timedelta(days=90))
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String, nullable=False)


    def serialize(vaccine_card):
        for keys, values in vaccine_card.items():
            vaccine_card[keys] = values.title()
        
        return vaccine_card


    @classmethod
    def validate_keys(cls, data: dict):
        expected_keys = {"cpf", "name", "vaccine_name", "health_unit_name"}
        request_keys = set(data.keys())
        invalid_keys = request_keys - expected_keys

        if invalid_keys:
            for key in invalid_keys:
                data.pop(key)

        elif len(expected_keys) != len(request_keys):
            raise KeyError(
                {
                    "expected_keys": list(expected_keys),
                    "invalid_sent_keys": list(invalid_keys)
                }
            )