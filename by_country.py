from flask import Flask, jsonify
import pandas
import numpy as np

app = Flask(__name__)

medals = pandas.read_csv("data/medals.csv", index_col=0)
medals = medals.dropna()


def by_country():
    array = pandas.DataFrame(medals.NOC.value_counts())
    countries = []
    for key, value in array.iterrows():
        countries.append({"country": key, "medals": value['NOC']})
    print(countries)


# by_country()


def by_medals():
    array = pandas.DataFrame(medals.Medal.value_counts())
    medals_count = []
    for key, value in array.iterrows():
        medals_count.append({'medal': key, 'count': value['Medal']})
    print(medals_count)


# by_medals()

def by_sport():
    array = pandas.DataFrame(medals.Sport.value_counts())
    sport_count = []
    for key, value in array.iterrows():
        sport_count.append({'sport': key, 'count': value['Sport']})
    print(sport_count)


#by_sport()
