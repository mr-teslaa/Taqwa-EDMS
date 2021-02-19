from os     import environ
from dotenv import load_dotenv
load_dotenv() # Load the ENV variables from the .env file

SECRET_KEY                     = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI        = 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False