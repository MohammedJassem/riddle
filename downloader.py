import os
import requests

# Create the "audio" directory if it doesn't exist
os.makedirs("audio", exist_ok=True)

# List of audio files (filename, url)
audio_files = [
    (
        "seer.mp3",
        "https://www.chosic.com/wp-content/uploads/2021/08/scott-buckley-i-walk-with-ghosts(chosic.com).mp3",
    ),
    (
        "clown.mp3",
        "https://www.chosic.com/wp-content/uploads/2022/10/Ghost-Story(chosic.com).mp3",
    ),
    (
        "magician.mp3",
        "https://www.chosic.com/wp-content/uploads/2025/01/Fantasy_Soundscape-chosic.com_.mp3",
    ),
    (
        "faceless.mp3",
        "https://www.chosic.com/wp-content/uploads/2022/10/Hitman(chosic.com).mp3",
    ),
    (
        "marionettist.mp3",
        "https://www.chosic.com/wp-content/uploads/2021/02/Unseen-Horrors(chosic.com).mp3",
    ),
    (
        "bizarro.mp3",
        "https://www.chosic.com/wp-content/uploads/2025/04/Punch-Deck-Code-Switch-chosic.com_.mp3",
    ),
    (
        "scholar.mp3",
        "https://www.chosic.com/wp-content/uploads/2022/07/Day-of-Chaos(chosic.com).mp3",
    ),
    (
        "miracle.mp3",
        "https://www.chosic.com/wp-content/uploads/2025/06/EyesInTheVoid-chosic.com_.mp3",
    ),
    (
        "attendant.mp3",
        "https://www.chosic.com/wp-content/uploads/2021/08/scott-buckley-i-walk-with-ghosts(chosic.com).mp3",
    ),
    (
        "fool.mp3",
        "https://cdn.pixabay.com/download/audio/2021/10/06/audio_3e0cfc41a5.mp3",
    ),
    (
        "completion.mp3",
        "https://store-screenapp-production.storage.googleapis.com/vid/68814bdc3768f6670f4c8f4a/85ef9758-f20a-40d7-96f5-840d09e2ba80.mp3",
    ),
]

# Set up a browser-like user-agent header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
}

# Download each audio file
for filename, url in audio_files:
    filepath = os.path.join("audio", filename)
    print(f"Downloading {filename}...")
    try:
        response = requests.get(url, stream=True, headers=headers, timeout=30)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"✅ Saved to {filepath}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")
