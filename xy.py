import pyautogui, time

print('Press Crtl-C to quit.')

try:
    while True:
        print (pyautogui.position())
        time.sleep(1)
        
except KeyboardInterrupt:
    print('\nDone.')
