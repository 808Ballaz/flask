from flask import Flask, render_template, request
import yelp_api
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ
import os
app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    business = None
    if address:
    	business = yelp_api.get_businesses(address,'food')
    return render_template('index.html', business=business)

@app.route("/about.html")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
