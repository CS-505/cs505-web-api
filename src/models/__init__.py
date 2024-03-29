from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .zipcode_distance import ZipCodeDistance
from .hospital_data import HospitalData
from .patient_data import PatientData
from .zip_alert import ZipAlert