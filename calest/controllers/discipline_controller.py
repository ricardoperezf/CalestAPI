import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas


# obtiene medallas por disciplina

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