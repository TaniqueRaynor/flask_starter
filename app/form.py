from random import choices
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField,SelectField
from wtforms.validators import DataRequired

PType = [(1, 'House'),(2, 'Apartment')]

class PropertyForm(FlaskForm):
  
    ptitle = StringField('Property Title', validators=[DataRequired()])
    rooms = StringField('No. of Rooms',validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms',validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    descr = TextAreaField('Description', validators=[DataRequired()])
    ptype  = SelectField('Property Type', choices=PType )
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])

