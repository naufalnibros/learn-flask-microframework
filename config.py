import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, "db_repository")

WTF_CSRF_ENABLED = True
SECRET_KEY = "tebak-aku"

OPENID_PROVIDERS = [
    {"name" : "Google", "url":"https://www.google.com/accounts/08/id"},
    {"name" : "flickr", "url":"https://www.flickr.com/<username>"},
]
