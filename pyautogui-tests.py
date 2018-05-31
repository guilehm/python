import pyautogui

pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(100, 200, duration=0.25)
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(800, 100, duration=0.25)
pyautogui.moveTo(400, 400, duration=0.25)
pyautogui.moveTo(100, 400, duration=0.25)

for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)