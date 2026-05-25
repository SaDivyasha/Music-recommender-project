import os
import platform
import cv2
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from deepface import DeepFace

# =====================================================================
# 1. HARDCODED CONFIGURATION & CREDENTIALS
# =====================================================================
# Hardcoded Spotify credentials from your configuration
SPOTIFY_CLIENT_ID = "466c881f1f1648749f26f92071b2973d"
SPOTIFY_CLIENT_SECRET = "4ce0219fda824710872c0b769980c9b6"

# Mood mapping dictionary to convert emotional states to search strings
MOOD_MAP = {
    "happy": "bollywood happy songs",
    "sad": "sad lofi songs",
    "angry": "motivational workout songs",
    "calm": "relaxing instrumental music",
    "energetic": "gym workout songs",
    "romantic": "romantic bollywood songs"
}

# Authenticate with Spotify API safely using your credentials
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager=auth_manager)

# =====================================================================
# 2. CORE UTILITY FUNCTIONS
# =====================================================================
def initialize_camera():
    """Initializes the webcam based on system platform requirements."""
    system = platform.system()
    if system == "Windows":
        # CAP_DSHOW resolves startup lag spikes on Windows architectures
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("⚠️ Default Camera Index 0 couldn't be opened. Trying index 1...")
        cap = cv2.VideoCapture(1)
        
    if not cap.isOpened():
        raise RuntimeError("Could not open any webcam interface handles.")
    return cap


def detect_mood(emotion):
    """Maps multi-class emotions down into your binary happy/sad tracking rules."""
    if emotion == "happy":
        return "happy"
    return "sad"


def get_spotify_recommendations(base_mood, query_modifier="", limit=10):
    """Queries Spotify using the mapped mood base and specific conversational keywords."""
    # Pull base query string from mood map dictionary
    base_query = MOOD_MAP.get(base_mood.lower(), "bollywood hits")
    
    # Combine standard base query with contextual user inputs
    if query_modifier:
        final_query = f"{base_query} {query_modifier}"
    else:
        final_query = base_query

    try:
        results = sp.search(q=final_query, type="track", limit=limit)
        songs = []
        for item in results["tracks"]["items"]:
            songs.append({
                "name": item["name"],
                "artist": item["artists"][0]["name"],
                "url": item["external_urls"]["spotify"]
            })
        return songs
    except Exception as e:
        print(f"Spotify API Search Error: {e}")
        return []


def recommend_playlist(mood):
    """Runs the interactive conversational phase and prints matching Spotify tracks."""
    print(f"\n➡ IRA detected your mood as: {mood.capitalize()}")

    query_modifier = ""

    # ---- HAPPY PATH ----
    if mood == "happy":
        print("\n✨ You look happy!")
        user_response = input(
            "Are you feeling enthusiastic, romantic, or chill?\n"
            "Tell me how you feel: "
        ).lower().strip()

        print("\n💬 IRA: Nice! Fetching a playlist curated for you from Spotify...")

        if "enthusiastic" in user_response or "excited" in user_response:
            query_modifier = "upbeat festival anthems"
        elif "romantic" in user_response or "love" in user_response:
            query_modifier = "acoustic love tracks"
        elif "chill" in user_response or "relax" in user_response:
            query_modifier = "lofi ambient chill"
        else:
            query_modifier = "feel good mix"

    # ---- SAD / THOUGHTFUL PATH ----
    else:
        print("\n☁️ You seem a little low.")
        user_response = input(
            "Are you feeling lonely or demotivated?\n"
            "Tell me what's on your mind: "
        ).lower().strip()

        print("\n💬 IRA: Thanks for sharing. Reaching out to Spotify for your tracks...")

        if "lonely" in user_response or "alone" in user_response:
            query_modifier = "comforting indie soft melodies"
        elif "demotivated" in user_response or "low" in user_response:
            query_modifier = "motivational healing soundtracks"
        else:
            query_modifier = "calm focus gentle waves"

    # ---- FETCH LIVE TRACKS FROM SPOTIFY ----
    songs = get_spotify_recommendations(base_mood=mood, query_modifier=query_modifier)

    if songs:
        print("\n🎵 ====== YOUR PERSONALIZED IRA PLAYLIST ======")
        for idx, song in enumerate(songs, 1):
            print(f"{idx}. {song['name']} by {song['artist']}")
            print(f"   🔗 Listen here: {song['url']}")
        print("================================================\n")
    else:
        print("\n❌ Could not retrieve tracks from Spotify. Please check your network connection.")


# =====================================================================
# 3. APPLICATION EXECUTION PATTERN
# =====================================================================
def main():
    detected_mood = None

    print("=" * 45)
    print("      IRA: THE SOUND OF YOU STARTED")
    print("   Look at the camera • Press Q to quit")
    print("=" * 45)

    try:
        cap = initialize_camera()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to read webcam frame.")
                break

            try:
                # Analyze frame expressions with DeepFace
                analysis = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)

                # Modern DeepFace payload structures array checks
                if isinstance(analysis, list):
                    emotion = analysis[0]["dominant_emotion"]
                else:
                    emotion = analysis["dominant_emotion"]

                # Process raw emotion tracking criteria down into happy vs sad paths
                detected_mood = detect_mood(str(emotion).lower().strip())

                # Draw UI Text Overlay on the Live Camera Feed Frame
                cv2.putText(
                    frame,
                    f"IRA Mood: {detected_mood.capitalize()}",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )

            except Exception:
                cv2.putText(
                    frame,
                    "Analyzing face...",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2,
                    cv2.LINE_AA,
                )

            # Show the live web cam rendering frame
            cv2.imshow("IRA - The Sound of You", frame)

            # Keep camera panel loop open until 'q' key is processed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        # Release video stream processing resources cleanly
        cap.release()
        cv2.destroyAllWindows()

        # Trigger recommendation interface flow
        if detected_mood:
            recommend_playlist(detected_mood)
        else:
            print("\nNo face detected clearly. Try again while looking at the camera.")

    except Exception as e:
        print(f"\nRuntime Error encountered: {e}")


if __name__ == "__main__":
    main()