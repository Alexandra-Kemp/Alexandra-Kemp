from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange



year_list = [('2019'), ('2020'), ('2021'), ('2022')]
qq_list = [('Q1'), ('Q2'), ('Q3'), ('Q4')]
emp_id_list = [('EMP244'), ('EMP256'), ('EMP234'), ('EMP267'), ('EMP290')]
product_id_list = [('PROD_001'), ('PROD_002'), ('PROD_003'), ('PROD_004'), ('PROD_005'), ('PROD_006'), ('PROD_007'), ('PROD_008')]
ESP_id_list = [('ESP_001'), ('ESP_002'), ('ESP_003'), ('ESP_004'), ('ESP_005'), ('ESP_006'), ('ESP_007'), ('ESP_008')]

class AddForm(FlaskForm):
    year = SelectField("Enter year: ", choices = [('2019'), ('2020'), ('2021'), ('2022')])
    qq = SelectField("Enter quarter: ", choices = [('Q1'), ('Q2'), ('Q3'), ('Q4')])
    week = IntegerField("Enter week: ", validators=[DataRequired(),NumberRange(min=0, max=51)])
    emp_id = SelectField('Employee ID: ', choices = emp_id_list)
    product_id = SelectField("Product ID: ", choices = product_id_list)
    p_quantity = IntegerField("Product Quantity: ")
    ESP_id = SelectField("ESP ID: ", choices = ESP_id_list)
    ESP_quantity = IntegerField("ESP Quantity: ")
    submit = SubmitField("ADD ENTRY")


class DelForm(FlaskForm):
    year = SelectField('Enter year: ', choices = year_list)
    qq = SelectField("Enter quarter: ", choices = qq_list)
    week = SelectField('Enter week: ', validators=[DataRequired(),NumberRange(min=0, max=51)])
    emp_id = SelectField('Employee ID: ', choices = emp_id_list)
    product_id = SelectField('Product ID: ', choices = product_id_list)
    submit = SubmitField('REMOVE ENTRY')
