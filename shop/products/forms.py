from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField,DecimalField,  TextAreaField, validators

class Addproducts(Form):
  name = StringField("Name", [validators.DataRequired()])
  price = DecimalField('Price', [validators.DataRequired()])
  discount = IntegerField('Discount', default=0)
  stock = IntegerField('Stock', [validators.DataRequired()])
  colors = TextAreaField('Color', [validators.DataRequired()])
  description = TextAreaField('Description', [validators.DataRequired()])

  image_1 = FileField('image 1', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_2 = FileField('image 2', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])
  image_3 = FileField('image 3', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])