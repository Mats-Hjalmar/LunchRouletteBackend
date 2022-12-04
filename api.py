from flask import Flask
from flask import json
from flask import request
import restaurant_repository

app = Flask(__name__)
PATH = "/api/lunch_roulette_v1/"

@app.route(PATH + "getAllRestaurants")
def get_all_restaurants():
    return json.jsonify(restaurant_repository.get_all_restaurants())

@app.route(PATH + "postLunchSelection", methods=['POST'])
def post_lunch():
    return json.jsonify({"link_url": restaurant_repository.get_meal_from_restaurant(json.loads(request.data)["id"])})

app.run()
