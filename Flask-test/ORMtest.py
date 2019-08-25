from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/db_amalProject'
db = SQLAlchemy(app)

class District(db.Model):
	__tablename__ = 'district'
	district_id = db.Column('district_id', db.Integer, primary_key=True)
	district_name = db.Column('district_name', db.Unicode)


districts = District.query.all()
print(districts)
for data in districts:
    print(data.district_name)