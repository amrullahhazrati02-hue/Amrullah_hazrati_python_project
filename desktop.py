import subprocess
import time
import pyautogui
subprocess.Popen("calc.exe")
time.sleep(2)
pyautogui.write("25*4")
pyautogui.press("enter")
time.sleep(2)
subprocess.Popen("notepad.exe")
time.sleep(2)

pyautogui.write("Desktop automation test complete successfully.")
time.sleep(1)
pyautogui.hotkey("de")
