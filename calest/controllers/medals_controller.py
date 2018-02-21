import pandas
from calest import calest_app
from flask import request, jsonify
from ..models.Medals import Medal


@calest_app.route('/discipline')
def get_discipline():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_discipline()
    return jsonify(result), 201


@calest_app.route('/gender')
def get_gender():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_gender()
    return jsonify(result), 201


@calest_app.route('/city')
def get_city():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_city()
    return jsonify(result), 201


@calest_app.route('/country')
def get_country():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_country()
    return jsonify(result), 201


@calest_app.route('/medal')
def get_medals():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_by_medals()
    return jsonify(result), 201


@calest_app.route('/sport')
def get_sport():
    csv_file = pandas.read_csv('/home/virtualizacion/CalestAPIr/CalestAPI/calest/data/medals.csv')
    result = Medal(csv_file).get_medals_by_sport()
    return jsonify(result), 201
