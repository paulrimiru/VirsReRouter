from flask import Flask
import requests

APP = Flask(__name__)

from app import views