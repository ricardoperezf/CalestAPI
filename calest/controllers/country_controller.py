import pandas
from calest import calest_app, client
from flask import request, jsonify
from ..models.Medals import Medal

db = client.estadisticas
collection = db.medallas

# obtiene medallas por pais

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
