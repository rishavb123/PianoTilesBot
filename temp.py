import pyautogui
import time
import keyboard

#open http://tanksw.com/piano-tiles/

game_box = pyautogui.locateOnScreen('start.png', confidence=0.5)

click_x = int(game_box.left + game_box.width * 0.25)
click_y = int(game_box.top + game_box.height / 6)

pyautogui.click(click_x, click_y)
letters = ['a', 's', 'd', 'f']
while True:
    box = None
    for l in letters:
        if box == None:
            box = pyautogui.locateOnScreen(l + '.png', confidence=0.9, region=(game_box.left, game_box.top + int(game_box.height / 2), game_box.width, int(game_box.height / 4)))
    if box != None:
        print(box)
        pyautogui.click(box.left + int(box.width / 2), box.top + int(box.height / 2))
    else:
        print("not found")
    if keyboard.is_pressed('r'):
        break