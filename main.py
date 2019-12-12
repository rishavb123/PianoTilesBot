import pyautogui
import time
import keyboard
import mss
import sys
import cv2
import numpy as np

#open http://tanksw.com/piano-tiles/

game_box = pyautogui.locateOnScreen('start.png', confidence=0.5)

if game_box == None:
    print("Game Not Found")
    sys.exit()

mode = 'Arcade'

if mode == 'Arcade':
    click_x = int(game_box.left + game_box.width * 0.75)
    click_y = int(game_box.top + game_box.height / 6)
elif mode == 'Zed':
    click_x = int(game_box.left + game_box.width * 0.25)
    click_y = int(game_box.top + game_box.height / 2)

sct = mss.mss()

monitor = {"top": int(game_box.top + 0.711 * game_box.height), "left": game_box.left, "width": game_box.width, "height": 1}

pyautogui.click(click_x, click_y)
click_y = int(game_box.top + game_box.height * 0.725)

monitor["top"] = int(click_y - game_box.height / 4 + 200)

run = False

score = 0

while True:

    if keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('d') or keyboard.is_pressed('f') or keyboard.is_pressed('p'):
        run = True

    if not run: continue

    # last_time = time.time()

    img = np.array(sct.grab(monitor))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    # print("\r" + str(score), end = "")

    count = 0

    click_x = -10

    for i in range(4):
        if img[0][int(len(img[0]) * (1 + 2 * i)/ 8)] < 70:
            click_x = int(game_box.left + game_box.width * (1 + 2 * i) / 8)
            count += 1

    if count == 1:
        pyautogui.click(click_x, click_y)
        score += 1

    # cv2.imshow("Stream", img)

    # print("fps: {}".format(1 / (time.time() - last_time)), min([img[len(img) - 1][int(len(img[0]) * (1 + 2 * i)/ 8)] for i in range(4)]))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

    if keyboard.is_pressed('r'):
        cv2.destroyAllWindows()
        break