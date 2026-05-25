# import platform
# import cv2
# from deepface import DeepFace


# # -------------------------------
# # Camera setup (cross-platform)
# # -------------------------------
# def initialize_camera():
#     system = platform.system()

#     if system == "Windows":
#         cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#     else:
#         cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         raise RuntimeError(
#             "Could not open webcam. Check camera permissions or try another camera index."
#         )

#     return cap


# # -------------------------------
# # Emotion mapping
# # -------------------------------
# def get_display_mood(emotion):
#     if emotion in ["happy"]:
#         return "Happy (Smiling)"
#     elif emotion in ["sad", "neutral"]:
#         return "Sad"
#     else:
#         return emotion.capitalize()


# # -------------------------------
# # Playlist recommendation
# # -------------------------------
# def recommend_playlist(emotion):
#     print(f"\n➡ IRA detected your mood as: {get_display_mood(emotion)}")

#     # Happy
#     if emotion in ["happy", "surprise"]:
#         print("\n✨ You look bright!")
#         user_response = input(
#             "Are you feeling enthusiastic, romantic, energetic, or chill?\n"
#             "Tell me how you feel: "
#         ).lower().strip()

#         print(
#             "\n💬 IRA: Great! Glad you're feeling good."
#             "\nHere’s a playlist to match your vibe:"
#         )

#         if "enthusiastic" in user_response or "excited" in user_response:
#             print("🎵 Playlist: Festival Anthems – upbeat & high tempo")
#         elif "romantic" in user_response or "love" in user_response:
#             print("🎵 Playlist: Acoustic Melodies & Love Tracks")
#         elif "energetic" in user_response or "hype" in user_response:
#             print("🎵 Playlist: Workout Energy & Heavy Bass")
#         elif "chill" in user_response or "relax" in user_response:
#             print("🎵 Playlist: Lo-Fi Beats & Ambient Chill")
#         else:
#             print("🎵 Playlist: Feel-Good Mix")

#     # Sad / neutral
#     elif emotion in ["sad", "neutral"]:
#         print("\n☁️ You seem thoughtful.")
#         user_response = input(
#             "Are you feeling lonely or demotivated?\n"
#             "Tell me what’s on your mind: "
#         ).lower().strip()

#         print(
#             "\n💬 IRA: Thanks for sharing."
#             "\nHere’s something chosen for your mood:"
#         )

#         if "lonely" in user_response or "alone" in user_response:
#             print("🎵 Playlist: Comforting Indie & Soft Melodies")
#         elif (
#             "demotivated" in user_response
#             or "sad" in user_response
#             or "low" in user_response
#         ):
#             print("🎵 Playlist: Motivational Healing Soundtracks")
#         else:
#             print("🎵 Playlist: Calm Focus & Gentle Waves")

#     # Other
#     else:
#         print(
#             f"\n🎵 Playlist: Balanced emotional playlist for feeling {emotion}"
#         )


# # -------------------------------
# # Main
# # -------------------------------
# def main():
#     dominant_emotion = None

#     print("=" * 45)
#     print("      IRA: THE SOUND OF YOU STARTED")
#     print("   Look at the camera • Press Q to quit")
#     print("=" * 45)

#     try:
#         cap = initialize_camera()

#         while True:
#             ret, frame = cap.read()

#             if not ret:
#                 print("Failed to read webcam frame.")
#                 break

#             try:
#                 analysis = DeepFace.analyze(
#                     frame,
#                     actions=["emotion"],
#                     enforce_detection=False,
#                 )

#                 # DeepFace compatibility
#                 if isinstance(analysis, list):
#                     dominant_emotion = analysis[0]["dominant_emotion"]
#                 else:
#                     dominant_emotion = analysis["dominant_emotion"]

#                 display_mood = get_display_mood(dominant_emotion)

#                 cv2.putText(
#                     frame,
#                     f"IRA Mood: {display_mood}",
#                     (20, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     1,
#                     (0, 255, 0),
#                     2,
#                     cv2.LINE_AA,
#                 )

#             except Exception:
#                 cv2.putText(
#                     frame,
#                     "Analyzing face...",
#                     (20, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     1,
#                     (0, 0, 255),
#                     2,
#                     cv2.LINE_AA,
#                 )

#             cv2.imshow("IRA - The Sound of You", frame)

#             if cv2.waitKey(1) & 0xFF == ord("q"):
#                 break

#         cap.release()
#         cv2.destroyAllWindows()

#         if dominant_emotion:
#             recommend_playlist(dominant_emotion)
#         else:
#             print(
#                 "\nNo face detected clearly."
#                 "\nTry again while facing the camera."
#             )

#     except Exception as e:
#         print(f"\nError: {e}")


# if __name__ == "__main__":
#     main()

import platform
import cv2
from deepface import DeepFace


# -------------------------------
# Camera setup (cross-platform)
# -------------------------------
def initialize_camera():
    system = platform.system()

    if system == "Windows":
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    else:
        cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError(
            "Could not open webcam. Check camera permissions."
        )

    return cap


# -------------------------------
# ONLY 2 emotions
# Happy = smiling/laughing
# Everything else = sad
# -------------------------------
def detect_mood(emotion):
    if emotion == "happy":
        return "happy"
    return "sad"


# -------------------------------
# Playlist recommendation
# -------------------------------
def recommend_playlist(mood):
    print(f"\n➡ IRA detected your mood as: {mood.capitalize()}")

    # HAPPY FLOW
    if mood == "happy":
        print("\n✨ You look happy!")

        try:
            lonelyuser_response = input("Your mood: ").lower().strip()
        except KeyboardInterrupt:
            print("\nInput cancelled.")
            return
        print("\n💬 IRA: Nice! Here's a playlist for you:")

        if "enthusiastic" in user_response:
            print("🎵 Playlist: Festival Anthems – upbeat & high tempo")

        elif "romantic" in user_response:
            print("🎵 Playlist: Acoustic Melodies & Love Tracks")

        elif "chill" in user_response:
            print("🎵 Playlist: Lo-Fi Beats & Ambient Chill")

        else:
            print("🎵 Playlist: Feel-Good Mix")

    # SAD FLOW
    else:
        print("\n☁️ You seem a little low.")

        user_response = input(
            "\nAre you feeling lonely or demotivated?\n"
            "Your mood: "
        ).lower().strip()

        print("\n💬 IRA: Thanks for sharing. Here's something for you:")

        if "lonely" in user_response:
            print("🎵 Playlist: Comforting Indie & Soft Melodies")

        elif "demotivated" in user_response:
            print("🎵 Playlist: Motivational Healing Soundtracks")

        else:
            print("🎵 Playlist: Calm Focus & Gentle Waves")


# -------------------------------
# Main
# -------------------------------
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
                analysis = DeepFace.analyze(
                    frame,
                    actions=["emotion"],
                    enforce_detection=False,
                )

                # compatibility with DeepFace output
                if isinstance(analysis, list):
                    emotion = analysis[0]["dominant_emotion"]
                else:
                    emotion = analysis["dominant_emotion"]

                # only happy/sad
                detected_mood = detect_mood(emotion)

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

            cv2.imshow("IRA - The Sound of You", frame)

            # Press Q to stop detection
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

        if detected_mood:
            recommend_playlist(detected_mood)
        else:
            print(
                "\nNo face detected clearly."
                "\nTry again while facing the camera."
            )

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()