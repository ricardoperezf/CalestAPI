import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas


# obtiene medallas por ciudad

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
