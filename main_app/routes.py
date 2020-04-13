from flask import render_template, jsonify, flash, redirect, url_for, request
from main_app import app



@app.route('/')
def index():
    return render_template('index.html')