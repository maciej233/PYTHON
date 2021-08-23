from flask import Blueprint
from website import authorization
from .models import User

auth = Blueprint('auth', __name__)

