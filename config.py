import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    if os.environ.get('DB_HOST'):
        SQLALCHEMY_DATABASE_URI = (
            f"""mysql+pymysql://{os.environ.get('DB_USERNAME')}:"""
            f"""{os.environ.get('DB_PASSWORD')}@"""
            f"""{os.environ.get('DB_HOST')}/"""
            f"""{os.environ.get('BLOG_DATABASE_NAME')}"""
        )
    else:
        load_dotenv(verbose=True, dotenv_path="test.env")
        SQLALCHEMY_DATABASE_URI = (
            f"""mysql+pymysql://{os.environ.get('DB_USERNAME')}:"""
            f"""{os.environ.get('DB_PASSWORD')}@"""
            f"""{os.environ.get('DB_HOST')}/"""
            f"""{os.environ.get('BLOG_DATABASE_NAME')}"""
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
