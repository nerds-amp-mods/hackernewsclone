# !usr/bin/env python3
import os
from flask import Flask, request
import requests
from bs4 import beautifulsoup
from google.cloud import datastore



app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello World'

if __name__ == '__main__':
	app.run(DEBUG=True)
