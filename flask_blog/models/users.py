from werkzeug.security import generate_password_hash, check_password_hash

from flask_blog import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    created_at = db.Column(db.DateTime)
    address = db.relationship('Entry')

    @classmethod
    def from_args(cls, username=str, password=str):
        instance = cls()
        instance.username = username
        if password is not None:
            instance.hash_password(password)
        return instance

    def hash_password(self, clean_password):
        self.password = generate_password_hash(str(clean_password), method='sha256')

    # def check_password(self, clean_password):
    #     return check_password_hash(self.password, clean_password)
