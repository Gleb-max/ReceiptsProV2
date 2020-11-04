import os


class Config:
    # App
    SECRET_KEY = os.urandom(24)

    # Database
    dirname = os.path.dirname(os.path.abspath(__file__))
    # print(f"sqlite:///{dirname}\\data.db")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{dirname}\\data.db")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
