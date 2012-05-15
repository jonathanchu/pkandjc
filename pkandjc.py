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
from flaskext.lesscss import lesscss

app = Flask(__name__)
app.debug = True
join_path = lambda p1,p2: os.path.abspath(os.path.join(p1,p2))
PROJECT = os.path.abspath(os.path.dirname(__file__))
app.static_path = join_path(PROJECT, 'static/less/lib/')
lesscss(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
