from app import app
from flask import render_template
from app.models import select_data
@app.route('/')
def index():
    dates = select_data()
    return render_template("index.html",component = dates)