from flask import Flask, flash, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from tables import *

app = Flask(__name__)
app.secret_key = "b1234567"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/db_amalProject'
db = SQLAlchemy(app)
class District(db.Model):
    __tablename__ = 'district'
    district_id = db.Column('district_id', db.Integer, primary_key=True)
    district_name = db.Column(db.String(50))
    
    def __init__(self,district_name):
        self.district_name = district_name


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert', methods=["POST"])
def insert():
    district = request.form.get("txt_district")
    new_district = District(district)
    db.session.add(new_district)
    db.session.commit()
    return redirect(url_for("index"))