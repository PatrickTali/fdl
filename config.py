import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))





load_dotenv(os.path.join(basedir, '.env'))





class Config():
    """"""

    FLASK_APP = os.environ.get('Flask_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY") or "nana nana"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  