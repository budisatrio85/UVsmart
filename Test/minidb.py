from google.appengine.ext import db


class MiniDB(db.Model):
    uv = db.StringProperty(required=False)
    ir = db.StringProperty(required=False)
    time = db.StringProperty(required=False)