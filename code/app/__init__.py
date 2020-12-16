from flask import Flask, request, url_for

from mainEngine import MainEngine
from flask_googlemaps import GoogleMaps

# Initialize the app
app = Flask(__name__, instance_relative_config=True)
app.secret_key='abcd1234'

mainEngine = MainEngine()
# for some reason if add the key its shows an error
gMap = GoogleMaps(app, key="{YOUR KEY HERE}")

# Load the views
from app import views
# Load the config file
app.config.from_object('config')
