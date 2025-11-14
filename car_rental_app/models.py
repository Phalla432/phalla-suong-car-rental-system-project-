# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime
import uuid

db = SQLAlchemy()

# Helper: JSON field
from sqlalchemy.types import TypeDecorator, TEXT
import json

class JSONEncodedDict(TypeDecorator):
    impl = TEXT
    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value
    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

# === MODELS ===

class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    id = db.Column(db.BigInteger, primary_key=True)
    uuid = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('superadmin','branch_manager','fleet_manager','support','auditor'), default='support')
    branch_id = db.Column(db.BigInteger)
    mfa_enabled = db.Column(db.Boolean, default=True)
    mfa_secret = db.Column(db.String(128))
    mfa_backup_codes = db.Column(db.Text)
    email_verified = db.Column(db.Boolean, default=False)
    verification_token = db.Column(db.String(64))
    reset_token = db.Column(db.String(64))
    reset_expires = db.Column(db.DateTime)
    last_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(45))
    last_login_branch = db.Column(db.String(100))
    failed_attempts = db.Column(db.Integer, default=0)
    locked_until = db.Column(db.DateTime)
    allowed_ips = db.Column(JSONEncodedDict)  # JSON
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.BigInteger)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))

    rentals = db.relationship('Rental', backref='user', lazy=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Car(db.Model):
    __tablename__ = 'cars'
    car_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price_per_day = db.Column(db.Numeric(10, 2))

    rentals = db.relationship('Rental', backref='car', lazy=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Rental(db.Model):
    __tablename__ = 'rentals'
    rental_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.car_id'))
    start_at = db.Column(db.Date)
    end_at = db.Column(db.Date)
    status = db.Column(db.String(50), default='reserved')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}