from flask import Flask, redirect, render_template, url_for
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from flask_migrate import Migrate
from sqlalchemy.sql.functions import user

from config import Config
from forms import LoginForm, RegisterForm
from models import db, User

migrate = Migrate()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
  return db.session.execute(db.select(User).where(User.id == user_id)).scalar_one_or_none()

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app)
  # Home Route
  @app.route('/')
  def home():
      return render_template('home.html')
  # Login Route
  @app.route('/login', methods=['GET', 'POST'])
  def login():
    form = LoginForm()
    if form.validate_on_submit():
      user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar_one_or_none()
      if user:
        if user.check_password(form.password.data):
          login_user(user)
          return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)
  # Register Route
  @app.route('/register', methods=['GET', 'POST'])
  def register():
    form = RegisterForm()
    if form.validate_on_submit():
      user = User(
        email=form.email.data,
        password=form.password.data
      )
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('login'))
    return render_template('register.html', form=form)
  # Logout Route
  @app.route('/logout', methods=['GET', 'POST'])
  @login_required
  def logout():
    logout_user()
    return redirect(url_for('home'))
  # Dashbord Route
  @app.route('/dashboard')
  @login_required
  def dashboard():
    user = current_user
    return render_template('dashboard.html', user=user)
  return app