import os
import time

import pyautogui
from PIL import ImageGrab

TAKE_PICTURE = bool(os.environ.get('TAKE_PICTURE', False))


def click(key, hold=False):
    if hold:
        pyautogui.keyDown(key)
        time.sleep(0.2)
        pyautogui.keyUp(key)
    else:
        pyautogui.press(key)
    return


def is_collision(pixels):
    # Check for birds
    for x in range(525, 585):
        for y in range(287, 288):
            if TAKE_PICTURE:
                pixels[x, y] = 100
            else:
                if pixels[x, y] < 171:
                    click("down", hold=True)
                    return

    # Check for cactus
    for x in range(525, 585):
        for y in range(319, 320):
            if TAKE_PICTURE:
                pixels[x, y] = 0
            else:
                if pixels[x, y] < 171:
                    click("up")
                    return
    return


if __name__ == "__main__":
    if TAKE_PICTURE:
        time.sleep(1)
    else:
        time.sleep(1)
        click('up')

    while True:
        # capture image in black & white format
        image = ImageGrab.grab().convert('L')
        image_pixels = image.load()
        is_collision(image_pixels)
        if TAKE_PICTURE:
            image.save('debug.png')
            print('image saved successfully')
            break
