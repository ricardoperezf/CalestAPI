#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
import pymongo as pymongo

calest_app = Flask(__name__)
uri = "mongodb://grupocosmosdb:Mbz2KwKHE8UBlSTrY8cDor7N7zWxHHjDxpbGjliuBwWNzGx5w5H862Z5H2kTnDDb9tR89WZa4H6cipfcS8L5Mw==@grupocosmosdb.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

from calest.controllers import *
