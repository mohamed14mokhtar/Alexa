import gtts
import vlc
import time
import os

# Generate the greeting audio

class sounds :
    text : str
    lang : str
    filename : str
    def __init__(self,text : str = "hello mohamed"
                 ,lang : str = "en" , filename : str = "welcome.mp3"):
        self.text = text
        self.lang = lang
        self.filename = filename
        
    # def generate_greeting(self):
    #     tts = gtts.gTTS(text= self.text, lang=self.lang, slow=False)
    #     tts.save(self.filename)
    #     print(f"[INFO] Audio saved as {self.filename}")
    
    def generate_greeting(self):
        if not self.text or not self.text.strip():
            print("[WARNING] No text provided for TTS, skipping audio generation.")
            return
    
        tts = gtts.gTTS(text=self.text, lang=self.lang, slow=False)
        tts.save(self.filename)
        print(f"[INFO] Audio saved as {self.filename}")

    # Play the generated audio using VLC
    def play_audio(self):
        
        if not os.path.exists(self.filename):
            print("[ERROR] File does not exist.")
            return
        player = vlc.MediaPlayer(self.filename)
        player.play()
        time.sleep(1)  # Give it time to start
        duration = player.get_length() / 1000  # in seconds
        print(f"[INFO] Playing audio for {duration:.2f} seconds")
        time.sleep(duration + 1)

if __name__ == "__main__":
    mohamed = sounds()
    mohamed.generate_greeting()
    mohamed.play_audio()