
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv

load_dotenv()
db = SQLAlchemy()

test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")

def create_app():
    app = Flask(__name__)  
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    db.init_app(app) 
    return app