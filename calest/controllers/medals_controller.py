import pandas
from calest import calest_app
from flask import request, jsonify
from ..models.Medals import Medal


@calest_app.route('/discipline', methods=["POST"])
def post_discipline():
    csv_received = request.files['file']
    csv_file = pandas.read_csv(csv_received)
    result = Medal(csv_file).get_medals_discipline()
    return jsonify(result), 201


@calest_app.route('/gender', methods=["POST"])
def post_gender():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_gender()
    return jsonify(result), 201


@calest_app.route('/city', methods=["POST"])
def post_city():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_city()
    return jsonify(result), 201


@calest_app.route('/country', methods=["POST"])
def post_country():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_country()
    return jsonify(result), 201


@calest_app.route('/medal', methods=["POST"])
def post_medals():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_by_medals()
    return jsonify(result), 201


@calest_app.route('/sport', methods=["POST"])
def post_sport():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_by_sport()
    return jsonify(result), 201
