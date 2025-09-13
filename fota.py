import website
import time
import pyautogui, sys

fota_padge  = website.Web(" http://127.0.0.1:1880/ui")

def open_fota_page():
    fota_padge.open_browser()
    time.sleep(2)
    
def jump_to_application():
    print("Jumping to application...")
    pyautogui.click(x=344, y=285)
    time.sleep(1)
    
def jump_to_bootloader():
    print("Jumping to bootloader...")
    fota_padge.open_browser()
    time.sleep(2)
    pyautogui.click(x=344, y=479)
    
def downloadCode():
    print("download code")
    fota_padge.open_browser()
    time.sleep(2)
    pyautogui.click(x=344, y=479) #application
    time.sleep(1)
    pyautogui.click(x=344, y=365) #sector erase
    time.sleep(1)
    pyautogui.click(x=344, y=479) #download code
    time.sleep(1)
    
def turnOn_led1():
    print("turn on led 1")
    pyautogui.click(x=758, y=365) #turn on led 1

def turnOff_led1():
    print("turn off led 1")
    pyautogui.click(x=758, y=285) #turn off led 1

def turnOn_led2():
    print("turn on led 2")
    pyautogui.click(x=1200, y=365) #turn on led 2
    
def turnOff_led2():
    print("turn off led 2")
    pyautogui.click(x=1200, y=285) #turn off led 2
    

    
if __name__ =="__main__":
    # open_fota_page()
    open_fota_page()
    jump_to_application()
    turnOn_led2()