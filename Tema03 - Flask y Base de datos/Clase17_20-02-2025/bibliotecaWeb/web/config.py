# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/biblioteca_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False