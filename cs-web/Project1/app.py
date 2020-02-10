from flask import Flask, render_template, request, session, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)
engine = create_engine("postgres://postgres:1234@localhost:5432/pr1")
db = scoped_session(sessionmaker(bind=engine))
app.config['SECRET_KEY'] = 'sadfaegadfaserafsdbfasf'

@app.route("/")
def index():
    if session.get('user') is None:
        return redirect('/login')
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('login.html')

@app.route('/relog', methods=['POST'])
def relog():
    if request.form.get('register') is not None:
        return "you registered"
    elif request.form.get('login') is not None:
        return "you logged in"
