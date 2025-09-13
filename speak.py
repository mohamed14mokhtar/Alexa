import speech_recognition as sr

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()  # fixed spelling
        
    def record_audio(self):
        with sr.Microphone() as source:
            print("🎤 Listening....")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        return audio
    
    def recognize_speech(self, audio) :
        try:
            text = self.recognizer.recognize_google(audio, language="EG")
            print(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ I couldn't understand what you said.")
        except sr.RequestError:
            print("❌ Network error or Google service not available.")
        return ""    
    
    def recognize_speech_with_return(self, audio) :
        try:
            text = self.recognizer.recognize_google(audio, language="EG")
            print(f"🗣️ You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ I couldn't understand what you said.")
        except sr.RequestError:
            print("❌ Network error or Google service not available.")
        return ""    
    
    

if __name__ == "__main__":
    listen = VoiceAssistant()
    audio = listen.record_audio()
    listen.recognize_speech(audio)