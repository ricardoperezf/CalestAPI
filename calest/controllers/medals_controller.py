import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas


@calest_app.route('/result', methods=["POST"])
def post_discipline():
    csv_received = request.files['file']
    csv_file = pandas.read_csv(csv_received)
    discipline_result = Medal(csv_file).get_medals_discipline()
    gender_result = Medal(csv_file).get_medals_gender()
    city_result = Medal(csv_file).get_medals_city()
    country_result = Medal(csv_file).get_medals_country()
    medals_result = Medal(csv_file).get_medals_by_medals()
    sport_result = Medal(csv_file).get_medals_by_sport()
    cursor = collection.insert({
        "discipline": discipline_result,
        "gender": gender_result,
        "city": city_result,
        "country": country_result,
        "medal": medals_result,
        "sport": sport_result
    })
    return jsonify("Added"), 201


@calest_app.route('/result', methods=["GET"])
def get_discipline():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'sport': medals["sport"],
            'discipline': medals["discipline"],
            'medals': medals["medal"],
            'city': medals["city"],
            'country': medals["country"],
            'gender': medals["gender"]
        })
    return jsonify(vector)
