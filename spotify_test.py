import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

try:

    client_id = "0817ce4ffb8940cf8937a2f899b301cb"
    client_secret = "bec74ef811904b94a70d04136b326eaf"

    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    sp = spotipy.Spotify(
        auth_manager=auth_manager
    )

    print("Spotify connected successfully!")

    results = sp.search(
        q="Believer",
        type="track",
        limit=1
    )

    print("Search completed!")

    print(results)

except Exception as e:

    print("ERROR OCCURRED:")
    print(e)