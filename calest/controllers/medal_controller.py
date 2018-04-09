import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas

# obtiene medallas por medallas

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
