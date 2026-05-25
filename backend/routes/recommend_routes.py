from flask import Blueprint
from flask import request
from flask import jsonify

from services.spotify_service import (
    get_spotify_recommendations
)

recommend_bp = Blueprint(
    "recommend",
    __name__
)


@recommend_bp.route(
    "/recommend",
    methods=["GET"]
)

def recommend():

    mood = request.args.get("mood")

    results = get_spotify_recommendations(
        mood
    )

    return jsonify(results)