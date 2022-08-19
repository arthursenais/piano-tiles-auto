import pyautogui as p
from PIL import ImageGrab


py = 485
px1 = 501
px2 = 568
px3 = 636
px4 = 707
cor = 1

while True:
    tecla1 = ImageGrab.grab().getpixel((px1,py))[0]
    tecla2 = ImageGrab.grab().getpixel((px2,py))[0]
    tecla3 = ImageGrab.grab().getpixel((px3,py))[0]
    tecla4 = ImageGrab.grab().getpixel((px4,py))[0]

    if tecla1 == cor:
        p.click(px1, py)
    if tecla2 == cor:
        p.click(px2, py)
    if tecla3 == cor:
        p.click(px3, py)
    if tecla4 == cor:
        p.click(px4, py)