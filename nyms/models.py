import os, os.path
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from nyms import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(
    os.path.join(app.root_path, 'acronyms.db'))

db = SQLAlchemy(app)


class Acronym(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), nullable=False)
    description = db.Column(db.String(140), nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    # Possible versioning
    #revision = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.date_created = self.date_modified = datetime.now()


    def __str__(self):
        return self.name


    def __repr__(self):
        desc_len = len(self.description)
        return '<{} {}: {}>'.format(self.__class__.__name__,
            self.name, self.description[:20] + ('...' if desc_len > 20 else ''))
