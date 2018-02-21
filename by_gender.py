from flask import Flask, jsonify
import pandas
import numpy as np

app = Flask(__name__)

medals = pandas.read_csv("data/medals.csv", index_col=0)
medals = medals.dropna()

def by_discipline():
    array = pandas.DataFrame(medals.Discipline.value_counts())
    discipline_count = []
    for key, value in array.iterrows():
        discipline_count.append({'discipline': key, 'count': value['Discipline']})
    print(discipline_count)


#by_discipline()

def by_gender():
    array = pandas.DataFrame(medals.Event_gender.value_counts())
    gender_count = []
    for key, value in array.iterrows():
        gender_count.append({'gender': key, 'count': value['Event gender']})
    print(gender_count)


#by_gender()

def by_medals_city():
    array = pandas.DataFrame(medals.City.value_counts())
    city_count = []
    for key, value in array.iterrows():
        city_count.append({'city': key, 'count': value['City']})
    print(city_count)


#by_medals_city()