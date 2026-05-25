import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from mood_map import MOOD_MAP

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
    )
)


def get_spotify_recommendations(mood="happy", limit=10):

    # ✅ SAFE FIX (prevents None error)
    query = MOOD_MAP.get((mood or "").lower(), "bollywood hits")

    results = sp.search(q=query, type="track", limit=limit)

    songs = []

    for item in results["tracks"]["items"]:
        songs.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "url": item["external_urls"]["spotify"]
        })

    return songs