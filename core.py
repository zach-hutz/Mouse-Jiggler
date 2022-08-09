# sourcery skip: for-index-underscore, while-to-for
import random
import pyautogui
import time
import sys
import math

pyautogui.FAILSAFE = False
numMin = None

xPos = pyautogui.position().x
yPos = pyautogui.position().y

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
while(True):
    x=0
    while(x<numMin):
        time.sleep(random.randint(0, 313))
        x+=1
    xPos = pyautogui.position().x
    yPos = pyautogui.position().y
    R = 400
    (x,y) = pyautogui.size()
    (X,Y) = pyautogui.position(x/2,y/2)
    pyautogui.moveTo(X+R,Y, duration=0)

    for i in range(360):
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)), duration=0)

    pyautogui.moveTo(xPos, yPos)
    for i in range(3):
        pyautogui.press("shift")
