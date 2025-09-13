import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
    
pyautogui.moveTo(100, 200)  # moves mouse to X of 100, Y of 200.
# 920 - 142
# 644 - 604
# 912 - 208

#anghami
#240 300
#432 564
#710 293
#396 546

#fota 
#344 285 jump to application
#344 497 jump to bootloader
#344 563 download code
#366 365 sector erase
#758 285 turn off led 1
#758 365 turn on led 1
#1200 285 turn off led 2
#1200 365 turn on led 2