from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .zipcode_distance import ZipCodeDistance
from .hospital_data import HospitalData
