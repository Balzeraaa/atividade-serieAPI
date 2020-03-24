import json
from flask import Blueprint, abort
from flask_restful import Resource, reqparse
from app.serie.models import Serie
from app import api, db

serie = Blueprint("serie", __name__)

parser = reqparse.RequestParser()

parser.add_argument("name", type=str)
parser.add_argument("genre", type=str)
parser.add_argument("seasons", type=int)
parser.add_argument("imdb", type=float)
parser.add_argument("active", type=bool)


@serie.route("/")
@serie.route("/home")
def home():
    return "Catálogo de Series"


class SeriesAPI(Resource):
    def get(self, id=None, page=1):
        if not id:
            series = Serie.query.paginate(page, 10).items
        else:
            series = [Serie.query.get(id)]
        if not series:
            abort(404)
        res = {}
        for s in series:
            res[s.id] = {"name": s.name, "genre": s.genre, "seasons": str(s.seasons), "imdb": str(s.imdb), "active": s.active}
        return json.dumps(res)

    def post(self):
        args = parser.parse_args()
        name = args["name"]
        genre = args["genre"]
        seasons = args["seasons"]
        imdb = args["imdb"]
        active = args["active"]

        s = Serie(name, genre, seasons, imdb, active)
        db.session.add(s)
        db.session.commit()
        res = {}
        res[s.id] = {"name": s.name, "genre": s.genre, "seasons": str(s.seasons), "imdb": str(s.imdb), "active": s.active}
        return json.dumps(res)

api.add_resource(
    SeriesAPI,
    '/api/serie',
    '/api/serie/<int:id>',
    '/api/serie/<int:id>/<int:page>'
)