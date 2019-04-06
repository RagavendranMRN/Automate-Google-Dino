from numpy import *
import pyautogui as pag
from PIL import ImageGrab,ImageOps
import time
class cordinates():
    replaybtn = (685,390)

def restartgame():
    pag.click(cordinates.replaybtn)

def pressspace():
    pag.keyDown('space')
    print("Jump")
    pag.keyUp('space')

def detectimage():
    box = (485,391,500,427)
    image = ImageGrab.grab(box)
    grabImage = ImageOps.grayscale(image)
    a = array(grabImage.getcolors())   
    print(a.sum())
    return a.sum()

def main():
    time.sleep(2)
    restartgame()
    while True:
        if(detectimage()!= 787):
            pressspace()
            time.sleep(0.15)

main()
