import pandas
from flask import jsonify, make_response, Response
from flask import jsonify


class Medal:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.vector = []

    def get_medals_discipline(self):
        array = pandas.DataFrame(self.csv_file.Discipline.value_counts())
        for key, value in array.iterrows():
            self.vector.append({'discipline': str(key), 'count': int(value['Discipline'])})
        return self.vector

    def get_medals_gender(self):
        array = pandas.DataFrame(self.csv_file.Event_gender.value_counts())
        for key, value in array.iterrows():
            self.vector.append({'gender': str(key), 'count': int(value['Event_gender'])})
        return self.vector

    def get_medals_city(self):
        array = pandas.DataFrame(self.csv_file.City.value_counts())
        for key, value in array.iterrows():
            self.vector.append({'city': str(key), 'count': int(value['City'])})
        return self.vector

    def get_medals_country(self):
        array = pandas.DataFrame(self.csv_file.NOC.value_counts())
        for key, value in array.iterrows():
            self.vector.append({"country": str(key), "medals": int(value['NOC'])})
        return self.vector

    def get_medals_by_medals(self):
        array = pandas.DataFrame(self.csv_file.Medal.value_counts())
        for key, value in array.iterrows():
            self.vector.append({'medal': str(key), 'count': int(value['Medal'])})
        return self.vector

    def get_medals_by_sport(self):
        array = pandas.DataFrame(self.csv_file.Sport.value_counts())
        for key, value in array.iterrows():
            self.vector.append({'sport': str(key), 'count': int(value['Sport'])})
        return self.vector
