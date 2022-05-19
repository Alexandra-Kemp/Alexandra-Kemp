#TEST
from forms import AddForm
from flask import Flask, render_template,url_for,redirect
from forms import AddForm, DelForm
#from wtforms import Stringfield, Selectfield, Integer, SubmitField
#from wtforms.validators import DataRequired, NumberRange
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

#######################################################
########SQL Database Section###########################
#######################################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:NewYork1422$@localhost/emp'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

######################################################
########### Models ###################################
######################################################

class emp(db.Model):
    __tablename__ = 'Employees'
    emp_id = db.Column(db.Text(length=10),primary_key=True)
    lead_name = db.Column(db.Text)
    paygrade = db.Column(db.Text)
    region = db.Column(db.Text)
    isfound = db.Column(db.Text)

    def __init__(self,emp_id, lead_name, paygrade, region, isfound):
        self.emp_id = emp_id
        self.lead_name = lead_name
        self.paygrade = paygrade
        self.region = region
        self.isfound = isfound

class items(db.Model):
    __tablename__ = 'Products_ESPs'
    product_id = db.Column(db.Text,primary_key=True)
    p_description = db.Column(db.Text)
    p_price = db.Column(db.Integer)
    ESP_id = db.Column(db.Text, primary_key=True)
    ESP_description = db.Column(db.Text)
    ESP_price = db.Column(db.Integer)

    def __init__(self, product_id, p_description, p_price, ESP_id, ESP_description, ESP_price):
        self.product_id = product_id
        self.p_description = p_description
        self.p_price = p_price
        self.ESP_id = ESP_id
        self.ESP_description = ESP_description
        self.ESP_price = ESP_price

#Weekly Report of Sales by Employee
class sales_of_products(db.Model):
    __tablename__ = "sales_byproduct_byemp"
    year = db.Column(db.Integer, primary_key=True)
    qq = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Text,primary_key=True)
    product_id = db.Column(db.Text,primary_key=True)
    p_quantity = db.Column(db.Integer)
    p_totalforweek = db.relationship('items', backref='sales_of_products')
    ESP_quantity = db.Column(db.Integer)
    ESP_totalforweek = db.relationship('items', backref='sales_of_products')


    def __init__(self,emp_id, year, week, product_id, p_quantity, p_totalforweek, ESP_totalforweek):
        self.emp_id = emp_id
        self.year = year
        self.week = week
        self.product_id = product_id
        self.p_totalforweek = p_totalforweek
        self.ESP_totalforweek = ESP_totalforweek

    def __repr__(self):
        return f"Employee: {self.emp_id} for week: {self.week} and year: {self.year} generated {self.p_totalforweek} for product:{self.product_id} and {self.ESP_totalforweek} for the corresponding warranty /n"

db.create_all()

######################################################
######## View Functions -- Have Forms ################
######################################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_sales():

    form = AddForm()

    if form.validate_on_submit():

        emp_id = form.emp_id.data
        year = form.year.data
        week = form.week.data
        product_id = form.product_id.data
        p_quantity = form.p_quantity.data
        ESP_quantity = form.ESP_quantity.data
        new_entry = sales_of_products(emp_id)
        db.session.add(new_entry)
        db.session.commit()

        return redirect(url_for('list_sales'))

    return render_template('add.html', form=form)


@app.route('/list')
def list_sales():

    entries = sales_of_products.query.all()
    return render_template('list.html',entries=entries)

@app.route('/delete', methods=['GET', 'POST'])
def del_sales():

    form = DelForm()

    if form.validate_on_submit():
        emp_id = form.emp_id.data
        year = form.year.data
        qq = form.qq.data
        week = form.week.data
        product_id = form.product_id.data
        del_entry = sales_of_products.query.get(new_entry)
        db.session.delete(del_entry)
        db.session.commit()

        return redirect(url_for('list_sales'))

    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
