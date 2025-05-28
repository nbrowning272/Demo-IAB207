from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed, FileRequired, FileField
ALLOWED_FILE = {'PNG','JPG','png','jpg'}

class DestinationForm(FlaskForm):
  name = StringField('Country', validators=[InputRequired()])
  # adding two validators, one to ensure input is entered and other to check if the 
  # description meets the length requirements
  description = TextAreaField('Description', validators = [InputRequired()])
  image = FileField('Cover Image', validators=[FileRequired(message='Image cannot be empty'),FileAllowed(ALLOWED_FILE, message='Only PNG or JPG files allowed')])
  currency = StringField('Currency', validators=[InputRequired()])
  submit = SubmitField("Create")
    
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired('Enter Username')])
  password = PasswordField('Password', validators=[InputRequired('Enter Password')])
  submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[InputRequired()])
  email = EmailField('Email', validators=[Email('Please enter a valid email')])
  password = PasswordField('Password', validators=[InputRequired(), Length(min = 6), EqualTo('confirm_password', message = "Passwords must match")])
  confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min = 6)])
  submit = SubmitField('Register')


