from flask import Blueprint
from flask import request
from flask import jsonify

import pandas as pd


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    "backend/data/songs.csv"
).head(5000)

df = df.dropna()

df = df[[
    'track_name',
    'artists',
    'track_genre',
    'danceability',
    'energy',
    'valence'
]]


# =========================
# BLUEPRINT
# =========================

recommend_bp = Blueprint(
    "recommend",
    __name__
)


# =========================
# RECOMMEND FUNCTION
# =========================

def recommend_by_mood(mood):

    mood = mood.lower()


    if mood == "happy":

        filtered = df[
            (df["valence"] > 0.7)
        ]


    elif mood == "sad":

        filtered = df[
            (df["valence"] < 0.3)
        ]


    elif mood == "energetic":

        filtered = df[
            (df["energy"] > 0.8)
        ]


    elif mood == "party":

        filtered = df[
            (df["danceability"] > 0.8)
        ]


    elif mood == "calm":

        filtered = df[
            (df["energy"] < 0.4)
        ]


    else:

        return []


    filtered = filtered.head(5)

    recommendations = []


    for _, row in filtered.iterrows():

        recommendations.append({

            "song": row["track_name"],

            "artist": row["artists"],

            "genre": row["track_genre"]

        })


    return recommendations


# =========================
# API ROUTE
# =========================

@recommend_bp.route(
    "/recommend",
    methods=["GET"]
)

def recommend():

    mood = request.args.get("mood")

    results = recommend_by_mood(mood)

    return jsonify(results)