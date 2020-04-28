# note - using a MySQL database here, not SQLite
import pymysql
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
application = app

app.config['SECRET_KEY'] = 'sOmebiGseCretstrIng'

# connect to MySQL database on Reclaim
username = 'michae63_hs'
password = 'w8Sq3!8GCl;uG4'
userpass = 'mysql+pymysql://' + username + ':' + password + '@'
# this is for connection on the server
server  = 'michaelsclarks.com'
# change to YOUR database name, with a slash added as shown
dbname   = '/michae63_highschooldatabase'
# no socket

# setup required for SQLAlchemy and Bootstrap
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

db = SQLAlchemy(app)


# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# this database has only ONE table, socks
# identify all of your columns by name and data type as shown
class Fund(db.Model):
    __tablename__ = 'state_funds'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String)
    state = db.Column(db.String)
    edu_gen_funds = db.Column(db.Integer)
    edu_fed_funds = db.Column(db.Integer)
    edu_other_state_funds = db.Column(db.Integer)
    edu_bond_funds = db.Column(db.Integer)
    edu_total_funds = db.Column(db.Integer)

class School(db.Model):
    __tablename__ = 'hs_stats'
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String)
    location = db.Column(db.String)
    state = db.Column(db.String)
    rating = db.Column(db.String)
    state_test = db.Column(db.String)
    population = db.Column(db.String)
    grad_rate = db.Column(db.String)
    standard_test = db.Column(db.String)
    act_sat = db.Column(db.String)
    ap_class = db.Column(db.String)
    ap_pass = db.Column(db.String)
    white = db.Column(db.String)
    black = db.Column(db.String)
    hispanic = db.Column(db.String)
    asian = db.Column(db.String)
    native = db.Column(db.String)
    hawaiian = db.Column(db.String)
    twoplus = db.Column(db.String)

#class State(db.Model):
    #__tablename__ = 'state_stats'
    #id = db.Column(db.Integer, primary_key=True)
    #state = db.Column(db.String)
    #year10_11 = db.Column(db.String)
    #year11_12 = db.Column(db.String)
    #year12_13 = db.Column(db.String)
    #year13_14 = db.Column(db.String)
    #year14_15 = db.Column(db.String)
    #year15_16 = db.Column(db.String)
    #year16_17 = db.Column(db.String)
    #white = db.Column(db.String)
    #black = db.Column(db.String)
    #hispanic = db.Column(db.String)
    #asian = db.Column(db.String)
    #indian = db.Column(db.String)
    #twoplus = db.Column(db.String)
    #disability = db.Column(db.String)
    #limited_eng = db.Column(db.String)
    #econ_dis = db.Column(db.String)

# get sock IDs and names for the select menu BELOW
funds = Fund.query.order_by(Fund.state).all()
# create the list of tuples needed for the choices value
pairs_list = []
for fund in funds:
    pairs_list.append( (fund.id, fund.state) )

# Flask-WTF form magic
# set up the quickform - select includes value, option text (value matches db)
# all that is in this form is one select menu and one submit button
class StateSelect(FlaskForm):
    select = SelectField( 'Choose a state:',
      choices=pairs_list
      )
    submit = SubmitField('Submit')


# routes

# starting page for app
@app.route('/')
def index():
    # make an instance of the WTF form class we created, above
    form = StateSelect()
    # pass it to the template
    return render_template('index.html', form=form)


# whichever id comes from the form, that one sock will be displayed
@app.route('/funds', methods=['POST'])
def state_detail():
    fund_id = request.form['select']
    # get all columns for the one sock with the supplied id
    the_fund = Fund.query.filter_by(id=fund_id).first()
    the_school = School.query.filter_by(state=the_fund.state).all()
    # pass them to the template
    return render_template('statefund.html', the_fund=the_fund, the_school=the_school)

#@app.route('/school/<num>')
#def school_detail(num):
    #fund_id = request.form['select']
    #the_fund = Fund.query.filter_by(id=fund_id).first()
    #school_info = School.query.filter_by(state=the_fund.state).all()
    #return render_template('schoolname.html', the_fund=the_fund, school_info=school_info)


if __name__ == '__main__':
    app.run(debug=True)
