from flask import render_template
from flask import request
from app import app, pages


@app.route('/')
def home():
    return render_template('index.html')
