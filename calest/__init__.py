#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
import pymongo as pymongo

calest_app = Flask(__name__)
uri = "mongodb://proyecto:Ja8893rZtsv8nYNhRQ0rwvxDcurJWX4i8LORqb02YuvH6vu9tFl1gjU8ftzvkVb2TmjzDQN8JargYPWV0LPuGQ==@proyecto.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

from calest.controllers import *
