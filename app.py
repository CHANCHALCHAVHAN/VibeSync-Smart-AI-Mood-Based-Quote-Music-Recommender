from flask import Flask, render_template, jsonify, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    mood_input = request.json.get('mood', '').lower()

    # Define emotion patterns
    mood_patterns = {
        "happy": r"\b(happy|joyful|excited|glad|cheerful|elated)\b",
        "sad": r"\b(sad|low|depressed|down|lonely|heartbroken)\b",
        "angry": r"\b(angry|frustrated|annoyed|mad|irritated|furious)\b",
        "anxious": r"\b(anxious|stressed|nervous|worried|panicked|tense)\b"
    }

    # Initialize response values
    music_link = ""
    music_spotify_link = ""
    quote = ""
    affirmation = ""
    emoji = ""

    matched_mood = None
    for emotion, pattern in mood_patterns.items():
        if re.search(pattern, mood_input):
            matched_mood = emotion
            break

    # Mood-boosting logic
    if matched_mood == "sad":
        # Suggest happy content to uplift
        music_link = "Uplifting Happy Music Playlist"
        music_spotify_link = "https://open.spotify.com/playlist/37i9dQZF1DX4WsbXrYywt7"
        quote = '"Keep your face to the sunshine and you cannot see a shadow." — Helen Keller'
        affirmation = '"Happiness flows to me effortlessly."'
        emoji = "🌞"
    elif matched_mood == "happy":
        # Reinforce their happiness
        music_link = "Stay Happy Vibes Playlist"
        music_spotify_link = "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
        quote = '"The more you praise and celebrate your life, the more there is in life to celebrate." — Oprah Winfrey'
        affirmation = '"I radiate joy and gratitude every day."'
        emoji = "🎉"
    elif matched_mood == "angry":
        # Calm them down
        music_link = "Peaceful Mind Music Playlist"
        music_spotify_link = "https://open.spotify.com/playlist/37i9dQZF1DX6vYcnNqz4h0"
        quote = '"When anger rises, think of the consequences." — Confucius'
        affirmation = '"I breathe in peace, and let go of frustration."'
        emoji = "🧘"
    elif matched_mood == "anxious":
        # Calm and relax
        music_link = "Stress Relief Playlist"
        music_spotify_link = "https://open.spotify.com/playlist/37i9dQZF1DX9qXf1ntgd2w"
        quote = '"You don’t have to control your thoughts. You just have to stop letting them control you." — Dan Millman'
        affirmation = '"I am safe, calm, and grounded."'
        emoji = "🌿"
    else:
        # Mood not detected
        music_link = "Please enter a mood to get personalized recommendations."
        music_spotify_link = ""
        quote = ""
        affirmation = ""
        emoji = ""

    return jsonify({
        "music": music_link,
        "spotify_link": music_spotify_link,
        "quote": quote,
        "affirmation": affirmation,
        "emoji": emoji
    })

if __name__ == "__main__":
    app.run(debug=True)
