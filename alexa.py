import sound
import date_time
import website
import pyautogui
import time
import os 
import speak
import fota
import check_gemini
import google.generativeai as genai


# intialize sounds 
hello_message = sound.sounds("hello mohamed","en","welcome.mp3")
name = sound.sounds("mohamed mokhtar","en","name.mp3")
date_and_time = sound.sounds(date_time.text,"en","date.mp3")
led1_condution = sound.sounds("You have already turned on the led one once, there may be an error in the code.","en","led1_on.mp3")
led2_condution = sound.sounds("You have already turned on the led two once, there may be an error in the code.","en","led2_on.mp3")


# list of commands
list_of_commands = ["hello","name","date","time","open facebook"
                    ,"open youtube","open linkedin","open instagram"
                    ,"favorite show","quran","fota","f o t a","gemini"]
ret_word = ""


# intialize web
youtube  = website.Web("https://www.youtube.com")
linledin  = website.Web("https://www.linkedin.com")
instagram  = website.Web("https://www.instagram.com")
facebook = website.Web("https://www.facebook.com")
#fota_padge  = website.Web(" http://127.0.0.1:1880/ui")

# status = youtube.open_browser()
# time.sleep(5)    
# pyautogui.click(x=920, y=124)
# time.sleep(1)
# pyautogui.write('sabaho tahady', interval=0.25) 
# pyautogui.press('enter')  # press the Enter key
# time.sleep(1)
# pyautogui.click(x=632, y=208)
# time.sleep(2)
# pyautogui.click(x=644, y=604)
# time.sleep(2)
# pyautogui.click(x=1213, y=825)

# fota.turnOff_led2()

#initialize voice assistant
voice = speak.VoiceAssistant()
try:
    while 1:
        audio = voice.record_audio()
        text_audio = voice.recognize_speech(audio)

        # check if the text is in the list of commands
        for word in list_of_commands:
            if word in text_audio.lower():
                print(f"Command recognized: {word}")
                ret_word = str(word)
                break
            
            
        if ret_word == "hello":
            hello_message.generate_greeting()
            hello_message.play_audio()
        elif ret_word == "name":
            name.generate_greeting()
            name.play_audio()
        elif ret_word == "date":
            date_and_time.generate_greeting()
            date_and_time.play_audio()
        elif ret_word == "time":
            date_and_time.generate_greeting()
            date_and_time.play_audio()
        elif ret_word == "open facebook":    
            facebook.open_browser()
        elif ret_word == "open youtube":    
            youtube.open_browser()
        elif ret_word == "open linkedin":    
            linledin.open_browser()
        elif ret_word == "open instagram":
            instagram.open_browser()
        elif ret_word == "favorite show":
            print(" Opening favorite show on YouTube... ")
            status = youtube.open_browser()
            time.sleep(5)    
            pyautogui.click(x=920, y=124)
            time.sleep(1)
            pyautogui.write('sabaho tahady', interval=0.25) 
            pyautogui.press('enter')  # press the Enter key
            time.sleep(1)
            pyautogui.click(x=632, y=208)
            time.sleep(2)
            pyautogui.click(x=644, y=604)
            time.sleep(2
                       )
            pyautogui.click(x=1213, y=825)
        elif ret_word == "quran":
            os.system("start anghami:")
            time.sleep(4)    
            pyautogui.click(x=240 , y=300)
            time.sleep(1)
            pyautogui.click(x=432 , y=564)
            time.sleep(1)
            pyautogui.click(x=710 , y=293)
            time.sleep(1)
            pyautogui.click(x=396 , y=546)
        elif ret_word == "f o t a":
            fota_list = ["light one turn on ","light one turn off"
                         ,"light two turn on ","light two turn off"
                         ,"download code","exit","close"]
            led1_status = 0
            led2_status = 0
            while 1:
                audio = voice.record_audio()
                text_audio = voice.recognize_speech(audio)

                # check if the text is in the list of commands
                for word in fota_list:
                    if word in text_audio.lower():
                        print(f"Command recognized: {word}")
                        ret_word = str(word)
                        break
                
                if ret_word == "light one turn on ":
                    if led1_status == 0:
                        fota.turnOn_led1()
                        led1_status = 1
                    else:
                        led1_condution.generate_greeting()
                        led1_condution.play_audio()
                elif ret_word == "light one turn off":
                    fota.turnOff_led1()
                elif ret_word == "light two turn on ":
                    if led2_status == 0:
                        fota.turnOn_led2()
                        led2_status = 1
                    else:
                        led2_condution.generate_greeting()
                        led2_condution.play_audio()
                elif ret_word == "light two turn off":
                    fota.turnOff_led2()
                elif ret_word == "download code":
                    fota.downloadCode()
                elif "exit" in text_audio.lower() or "close" in text_audio.lower():
                    print("Exiting FOTA mode.")
                    break
                else:
                    print("No valid FOTA command recognized. Please try again.")
                time.sleep(1)
        elif ret_word == "gemini":
            # Configure once here (not every time)
            genai.configure(api_key="AIzaSyDzJxdHrHhHT_2-tdD-lD8jY5cY5pniMw4")

            while True:
                listen = speak.VoiceAssistant()
                audio = listen.record_audio()
                words = listen.recognize_speech(audio)
                
                if words:   # only run if speech recognized
                    check_gemini.generate(words)
                    time.sleep(2)
            
                    
        time.sleep(1)  # Give it time to start
        ret_word = ""
except KeyboardInterrupt:
    print("Voice assistant stopped by user.")
    
