from app import app
from flask import render_template,request,make_response
from app.models import select_data

@app.route('/',methods=['POST','GET'])
def login():
    #try:
    #    username = request.cookies.get('username')
    #except KeyError:
    #    resp = make_response(render_template("login.html"))
    #    resp.set_cookie('us')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['inputPassword']
        if username == 'nihao' and password == '123456':
            dates = select_data()
            resp = make_response(render_template('show.html',component = dates))
            resp.set_cookie('username',username)
            return resp
        else:
            return render_template("login.html")
    else:
        username = request.cookies.get('username')
        if username == 'nihao':
            dates = select_data()
            return  render_template('show.html',component = dates)
        return render_template("login.html")

@app.route('/show')
def show_db():
    dates = select_data()
    return  render_template("show.html",component = dates)