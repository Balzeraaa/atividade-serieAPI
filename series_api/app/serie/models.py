from app import db


class Serie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    genre = db.Column(db.String(30))
    seasons = db.Column(db.Integer)
    imdb = db.Column(db.Float(asdecimal=True))
    active = db.Column(db.Boolean)

    def __init__(self, name, genre, seasons, imdb, active):
        self.name = name
        self.genre = genre
        self.seasons = seasons
        self.imdb = imdb
        self.active = active

    def __repr__(self):
        return "Serie {0}".format(self.id)
