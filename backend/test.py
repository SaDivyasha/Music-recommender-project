import cv2
from deepface import DeepFace

# Initialize the webcam
cap = cv2.VideoCapture(1)

print("=============================================")
print("     IRA: THE SOUND OF YOU STARTED...       ")
print("  (Look at the camera. Press 'q' to quit)    ")
print("=============================================")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from webcam.")
        break

    try:
        # Analyze the frame for emotions
        # enforce_detection=False prevents the script from crashing if your face moves out of frame briefly
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        
        # DeepFace returns a list of dictionaries
        dominant_emotion = analysis[0]['dominant_emotion']
        
        # Map facial expressions to your project rules
        # Smiling -> Happy | Dull/Straight face -> Sad or Neutral
        if dominant_emotion in ['happy', 'surprise']:
            display_mood = "Happy (Smiling)"
        elif dominant_emotion in ['sad', 'neutral']:
            display_mood = "Sad (Dull/Straight Face)"
        else:
            display_mood = dominant_emotion.capitalize()

        # Display the detected emotion overlay on the webcam video feed
        cv2.putText(frame, f"IRA Mood: {display_mood}", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
    except Exception as e:
        cv2.putText(frame, "Analyzing face...", (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        dominant_emotion = None

    # Show the live webcam window
    cv2.imshow("IRA - The Sound of You", frame)

    # Break the loop immediately if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window before starting the interactive terminal prompt
cap.release()
cv2.destroyAllWindows()

# --- Interactive Recommendation Phase ---
if dominant_emotion:
    print(f"\n➡ IRA detected your initial state as: {display_mood}")
    # CASE 1: Happy / Smiling
    if dominant_emotion in ['happy', 'surprise']:
        print("\n✨ You look bright! Let's narrow down your vibe.")
        print("Are you feeling:")
        print("1. Enthusiastic")
        print("2. Romantic")
        print("3. Energetic")
        print("4. Light / Chill")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice == "1":
            print("\n🎵 Recommendation: Queueing up an upbeat, high-tempo festival playlist!")
        elif choice == "2":
            print("\n🎵 Recommendation: Dimming the lights. Playing acoustic melodies and soft love tracks.")
        elif choice == "3":
            print("\n🎵 Recommendation: Blasting heavy bass and high-energy workout anthems!")
        elif choice == "4":
            print("\n🎵 Recommendation: Relax. Streaming smooth lo-fi beats and casual ambient tracks.")
        else:
            print("\n🎵 Recommendation: Playing a generalized Feel-Good mix!")

    # CASE 2: Sad / Dull Straight Face
    elif dominant_emotion in ['sad', 'neutral']:
        print("\n☁️ You seem a bit low or deep in thought. What's on your mind?")
        print("Are you feeling:")
        print("1. Lonely")
        print("2. Demotivated")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        if choice == "1":
            print("\n🎵 Recommendation: Playing comforting, relatable indie melodies to accompany your thoughts.")
        elif choice == "2":
            print("\n🎵 Recommendation: Time for an upgrade. Triggering a powerful, rising motivational healing soundtrack!")
        else:
            print("\n🎵 Recommendation: Playing a gentle, calming background frequency to help you unwind.")
            
    # Fallback for unexpected angry/fear/disgust detections
    else:
        print(f"\n🎵 Recommendation: Playing a grounded, balanced emotional frequency playlist for feeling {dominant_emotion}.")
else:
    print("\nNo face data was processed. Try looking directly into the camera next time!")

    # --- Interactive Conversational Phase ---
if dominant_emotion:
    print(f"\n➡ IRA detected your initial state as: {display_mood}")
    
    # CASE 1: Happy / Smiling
    if dominant_emotion in ['happy', 'surprise']:
        print("\n✨ You look bright! Let's narrow down your vibe.")
        user_response = input("Are you feeling enthusiastic, romantic, energetic, or just light and chill? \nTell me how you feel: ").lower().strip()
        
        # Standard dynamic response for the happy category
        print("\n💬 IRA: Great... Its awesome that you feel nice today here is a playlist to make your mood more cheerful")
        
        # Specific sub-mood keyword routing
        if "enthusiastic" in user_response or "excited" in user_response:
            print("🎵 Playlist: [Enthusiastic Festival Anthems - Upbeat & High-Tempo]")
        elif "romantic" in user_response or "love" in user_response:
            print("🎵 Playlist: [Acoustic Melodies & Soft Midnight Love Tracks]")
        elif "energetic" in user_response or "hype" in user_response:
            print("🎵 Playlist: [High-Energy Workout & Heavy Bass Booster]")
        elif "light" in user_response or "chill" in user_response or "relax" in user_response:
            print("🎵 Playlist: [Smooth Lo-Fi Beats & Casual Ambient Air]")
        else:
            print("🎵 Playlist: [IRA's Choice - Universal Feel-Good Sunshine Mix]")

    # CASE 2: Sad / Dull Straight Face
    elif dominant_emotion in ['sad', 'neutral']:
        print("\n☁️ You seem a bit low or deep in thought.")
        user_response = input("Are you feeling lonely or demotivated right now? \nTell me what's on your mind: ").lower().strip()
        
        # Standard empathetic response for the sad category
        print("\n💬 IRA: We are sorry that you feel that way, here is a playlist solely designed for your current mood. we hope that you get past this emotion")
        
        # Specific sub-mood keyword routing
        if "lonely" in user_response or "alone" in user_response:
            print("🎵 Playlist: [Comforting Indie Frequencies & Relatable Melodies]")
        elif "demotivated" in user_response or "sad" in user_response or "low" in user_response:
            print("🎵 Playlist: [Rising From Ash - Powerful Motivational Healing Soundscapes]")
        else:
            print("🎵 Playlist: [Calm Focus & Gentle Grounding Waves]")
            
else:
    print("\nNo face data was processed. Try looking directly into the camera next time!")