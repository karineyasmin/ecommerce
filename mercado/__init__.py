from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from mercado import routes

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = "89a6edc0e506748ec7aa9863"
db.init_app(app)
