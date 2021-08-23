import website
from . import db
from flask import url_for
from werkzeug.security import check_password_hash, generate_password_hash

class ValidationError(ValueError):
    pass


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        self.password_hash = check_password_hash(password)

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(120), unique=True)
    mgmt_ip = db.Column(db.String(64), unique=True)

    def get_url(self):
        return url_for('sites.get_device', id=self.id, _external=True)

    def export_data(self):
        return {
            'url': self.get_url(),
            'hostname': self.hostname,
            'ip': self.mgmt_ip
        }

    def import_data(self, data):
        try:
            self.hostname = data['hostname']
            self.mgmt_ip = data['mgmt_ip']
        except ValidationError as e:
            raise ValueError(f"Missing or invalid argument: {e.args[0]}")
        return self

    def __repr__(self):
        return f"class: {Device}"