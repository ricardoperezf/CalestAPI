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

#obtiene todo

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

#obtiene medallas por deporte

@calest_app.route('/sport', methods=["GET"])
def get_discipline_sport():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'year': medals["year"]
            for medals in cursor:
                print(medals)
                vector.append({
            'sport': medals["sport"]
        })
        })
    return jsonify(vector)

#obtiene medallas por disciplina

@calest_app.route('/discipline', methods=["GET"])
def get_discipline_discipline():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'discipline': medals["discipline"]
        })
    return jsonify(vector)

#obtiene medallas por medallas

@calest_app.route('/medal', methods=["GET"])
def get_discipline_medal():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'medal': medals["medal"]
        })
    return jsonify(vector)

#obtiene medallas por ciudad

@calest_app.route('/city', methods=["GET"])
def get_discipline_city():
    cursor = collection.find()
    vector = []
    for medals in cursor:
       print(medals)
       vector.append({
            'city': medals["city"]
        })
    return jsonify(vector)

#obtiene medallas por pais

@calest_app.route('/country', methods=["GET"])
def get_discipline_country():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'country': medals["country"]
        })
    return jsonify(vector)

#obtiene medallas por genero

@calest_app.route('/gender', methods=["GET"])
def get_discipline_gender():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'gender': medals["gender"]
        })
    return jsonify(vector)
