from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, session

app = Flask(__name__)
engine = create_engine("postgres://crtcgdjlkhktmg:90632001386e479383c4aa853f7bd6a753cceb221da959c6fdfef781f32ccf19@ec2-35-172-85-250.compute-1.amazonaws.com:5432/ddaooqjva5pmf4")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    ver = db.execute("SELECT version();").first()
    return str(ver)
