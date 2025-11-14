# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Use PyMySQL instead of mysqlclient
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/car_rental"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")