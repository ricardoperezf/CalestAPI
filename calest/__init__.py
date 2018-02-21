#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

calest_app = Flask(__name__)

from calest.controllers import *
