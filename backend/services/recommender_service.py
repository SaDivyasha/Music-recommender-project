import pandas as pd


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    "backend/data/songs.csv"
).head(5000)


# =========================
# REMOVE EMPTY VALUES
# =========================

df = df.dropna()


# =========================
# KEEP IMPORTANT COLUMNS
# =========================

df = df[[
    'track_name',
    'artists',
    'track_genre',
    'danceability',
    'energy',
    'valence'
]]


# =========================
# MOOD RECOMMENDATION FUNCTION
# =========================

def recommend_by_mood(mood):

    mood = mood.lower()


    # HAPPY SONGS
    if mood == "happy":

        filtered = df[
            (df["valence"] > 0.7)
        ]


    # SAD SONGS
    elif mood == "sad":

        filtered = df[
            (df["valence"] < 0.3)
        ]


    # ENERGETIC SONGS
    elif mood == "energetic":

        filtered = df[
            (df["energy"] > 0.8)
        ]


    # PARTY SONGS
    elif mood == "party":

        filtered = df[
            (df["danceability"] > 0.8)
        ]


    # CALM SONGS
    elif mood == "calm":

        filtered = df[
            (df["energy"] < 0.4)
        ]


    else:

        return ["Mood not found"]


    # TAKE TOP 5 SONGS
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
# USER INPUT
# =========================

mood = input(
    "Enter mood (happy/sad/energetic/calm/party): "
)


# =========================
# GET RECOMMENDATIONS
# =========================

results = recommend_by_mood(mood)


# =========================
# SHOW RESULTS
# =========================

print("\nRecommended Songs:\n")


for item in results:

    if isinstance(item, str):

        print(item)

    else:

        print(
            "Song:", item["song"],
            "| Artist:", item["artist"],
            "| Genre:", item["genre"]
        )