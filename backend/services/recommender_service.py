from flask import Blueprint, request, jsonify
import pandas as pd

recommend_bp = Blueprint("recommend", __name__)

# LOAD DATA
df = pd.read_csv("data/songs.csv").head(5000)
df = df.dropna()

df = df[[
    'track_name',
    'artists',
    'track_genre',
    'danceability',
    'energy',
    'valence'
]]


@recommend_bp.route("/recommend", methods=["POST"])
def recommend():

    mood = request.json.get("mood").lower()

    if mood == "happy":
        filtered = df[df["valence"] > 0.7]

    elif mood == "sad":
        filtered = df[df["valence"] < 0.3]

    elif mood == "energetic":
        filtered = df[df["energy"] > 0.8]

    elif mood == "party":
        filtered = df[df["danceability"] > 0.8]

    elif mood == "calm":
        filtered = df[df["energy"] < 0.4]

    else:
        return jsonify({"error": "Mood not found"})

    filtered = filtered.head(5)

    results = []

    for _, row in filtered.iterrows():
        results.append({
            "song": row["track_name"],
            "artist": row["artists"],
            "genre": row["track_genre"]
        })

    return jsonify(results)