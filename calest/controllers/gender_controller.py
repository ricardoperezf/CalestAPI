import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas


# obtiene medallas por genero

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
