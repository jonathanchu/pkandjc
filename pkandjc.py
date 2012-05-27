#!/usr/bin/env python
# encoding: utf-8
"""
pkandjc.py

Created by Jonathan Chu on 2011-11-16.
Copyright (c) 2011 3atmospheres LLC. All rights reserved.
"""

import sys
import os

from flask import Flask, jsonify, render_template, request
from flask.ext.assets import Environment

app = Flask(__name__)
assets = Environment(app)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
