

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
