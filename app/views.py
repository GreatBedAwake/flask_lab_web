from app import app
from flask import render_template,request,make_response,redirect,url_for,session
from app.models import select_data,select_where_db,update_db,component
import re
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/index')
def index():
    if 'username' in session:
        return render_template("index.html")
    else:
        return render_template("login.html")
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
            #resp = make_response(render_template('index.html'))
            #resp.set_cookie('username',username)
            #return resp
            session['username'] = username
            session['shop']=';'
            return redirect(url_for('index'))
        else:
            return render_template("login.html")
    else:
       # username = request.cookies.get('username')
#        session['username']=' '
#        session['status']=' '
        if 'username' in session:
            if 'nihao' == session['username']:
                return redirect(url_for('index'))
        else:
           return render_template("login.html")

@app.route('/show',methods=['POST','GET'])
def show_db():
    if request.method == 'POST':
        if 'find_component' in request.form:
            find_component=request.form['find_component']
            dates=select_where_db(find_component)
        else:
            name = request.form['name']
            count = request.form['count']
            cookies=name+','+count+';'
            sessionshop=session['shop']+cookies
            session['shop']=sessionshop
            dates = select_data()
    else:
        dates = select_data()
    return  render_template("show.html",component = dates)

@app.route('/shop',methods=['POST','GET'])
def shop():
    if 'shop' in session:
        shopping=session['shop']
        name = re.findall(';(.*?),',shopping)
        count = re.findall(',(.*?);',shopping)
        component =[]
        i=0
        for data in name:
            m=select_where_db(data)
            h=list(m[0])
            h[3]=count[i]
            component.append(h)
            i=i+1
        if request.method=='POST':
            i=0
            for data in name:
                update_db(data,count[i])
                i=i+1
            session['shop']=';'

        return render_template("gouwuche.html",component=component)
    else:
        return 'no shop'
@app.route('/add',methods=['POST','GET'])
def add():
    if request.method=='POST':
        name=request.form['name']
        bi=request.form['brief_introduction']
        location=request.form['location']
        counts=request.form['counts']
        m=component(name,bi,location,counts)
        m.insert_data()
    return render_template("add.html")
