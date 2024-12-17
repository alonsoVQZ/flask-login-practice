from flask import Flask, render_template
from flask_migrate import Migrate

from config import Config
from forms import LoginForm
from models import db

migrate = Migrate()

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  migrate.init_app(app, db)
  @app.route('/')
  def hello_world():
      return render_template('home.html')
  @app.route('/login')
  def login():
    return render_template('login.html', form=LoginForm())
  @app.route('/register')
  def register():
    return render_template('register.html')
  return app