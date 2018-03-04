#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
import pymongo as pymongo

calest_app = Flask(__name__)
uri = "mongodb://registro:Ee5gUsZ8xwwgkJpBM6eMfBnRxsgp3ckTIRLcsaqofX0H71yvu405yW4zr83eF3119qBeU5VKPo1hsJ9WRLK6MQ==@registro.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

from calest.controllers import *
