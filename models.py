from app import db

class ShortUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortlink = db.Column(db.String(4), index=True, unique=True)
    link = db.Column(db.String(128))

    def __repr(self):
        return '<Shortened Url {} to {}'.format(shortlink, link)
