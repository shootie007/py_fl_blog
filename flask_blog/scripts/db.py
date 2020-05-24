from flask_script import Command
from flask_blog import db
import flask_blog


class InitDB(Command):
    "create database"

    def run(self):
        # db.create_app()
        # flask_blog.create_app()
        db.create_all()


class DropDB(Command):
    "drop database"

    def run(self):
        db.drop_all()
