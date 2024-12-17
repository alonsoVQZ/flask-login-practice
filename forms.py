from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  email = EmailField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])
  submit = SubmitField('Login')

class RegisterForm(FlaskForm):
  email = EmailField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])
  submit = SubmitField('Register')