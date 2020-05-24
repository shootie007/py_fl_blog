# SQLALCHEMY_DATABASE_URI = 'mysql:///flask_blog.db'
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# DEBUG = True
# SECRET_KEY = 'secret key'
# USERNAME = 'john'
# PASSWORD = 'due123'

# import os


class Config:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db-name}?charset=utf8'.format(**{
        # 'user': os.getenv('DB_USER', 'root'),
        # 'password': os.getenv('DB_PASSWORD', 'mvbm4956'),
        # 'host': os.getenv('DB_HOST', 'localhost'),
        'user': 'root',
        'password': 'mvbm4956',
        'host': 'localhost',
        'db-name': 'blog'
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    SECRET_KEY = 'abCD12'


# Config = DevelopmentConfig
