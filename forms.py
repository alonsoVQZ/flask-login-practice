from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from models import db, User

class LoginForm(FlaskForm):
  email = EmailField('email', validators=[DataRequired()], render_kw={'placeholder': 'Email'})
  password = PasswordField('password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
  submit = SubmitField('Login')

class RegisterForm(FlaskForm):
  email = EmailField('email', validators=[DataRequired()], render_kw={'placeholder': 'Email'})
  password = PasswordField('password', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
  submit = SubmitField('Register')
  def validate_email(self, email):
    if db.session.execute(db.select(User).where(User.email == email.data)).scalar_one_or_none():
      raise ValidationError('Email alredy in use')