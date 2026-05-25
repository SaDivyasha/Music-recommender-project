from flask import Flask, request, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    mood = data.get("mood", "")
    language = data.get("language", "")
    artist = data.get("artist", "")

    # combine search
    query = f"{mood} {language} {artist}"

    results = sp.search(
        q=query,
        type="track",
        limit=10
    )

    songs = []

    for track in results["tracks"]["items"]:
        songs.append({
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"]
        })

    return jsonify(songs)


if __name__ == "__main__":
    app.run(debug=True)