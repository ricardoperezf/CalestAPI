import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas


# obtiene medallas por deporte

@calest_app.route('/sport', methods=["GET"])
def get_discipline_sport():
    cursor = collection.find()
    vector = []
    for medals in cursor:
        print(medals)
        vector.append({
            'sport': medals["sport"]
        })
    return jsonify(vector)
