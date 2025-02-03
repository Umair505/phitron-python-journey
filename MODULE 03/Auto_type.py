import pyautogui
from time import sleep
sleep(5)
for i in range(0,3):
    pyautogui.write('I love you python',interval=0.24)
    pyautogui.press('enter')

