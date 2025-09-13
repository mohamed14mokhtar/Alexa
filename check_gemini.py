# pip install google-generativeai

import base64
import mimetypes
import os
import google.generativeai as genai
import sound
import speak
import time


def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"File saved to: {file_name}")


def generate(words: str):
    # configure with API key (do it once per run, not in every loop ideally)
    # genai.configure(api_key="YOUR_API_KEY_HERE")

    # Load the model
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Send input prompt
    response = model.generate_content(
        words,   # now comes directly as parameter
        stream=True
    )

    file_index = 0
    for chunk in response:
        if not chunk.candidates:
            continue
        part = chunk.candidates[0].content.parts[0]

        if hasattr(part, "inline_data") and part.inline_data.data:
            file_name = f"output_{file_index}"
            file_index += 1
            inline_data = part.inline_data
            data_buffer = inline_data.data
            file_extension = mimetypes.guess_extension(inline_data.mime_type)
            save_binary_file(f"{file_name}{file_extension}", data_buffer)

        elif hasattr(part, "text"):
            print(part.text)
            mes = sound.sounds(text=part.text,
                               filename="gemini_response.mp3",
                               lang="en")
            mes.generate_greeting()
            mes.play_audio()


if __name__ == "__main__":
    try:
        # Configure once here (not every time)
        genai.configure(api_key="AIzaSyDzJxdHrHhHT_2-tdD-lD8jY5cY5pniMw4")

        while True:
            listen = speak.VoiceAssistant()
            audio = listen.record_audio()
            words = listen.recognize_speech(audio)

            if words:   # only run if speech recognized
                generate(words)

            time.sleep(2)

    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)