import pyautogui
import time

print(pyautogui.position())
pyautogui.rightClick(1306, 1052, duration=0.5) # Right click on chrome browser
pyautogui.click(1172,813, duration=0.5) # Opening a new tab
pyautogui.click(1206,94, duration=0.5) # Clicking on the search bar
pyautogui.write('https://sudoku.com/') # Entering the sudoku site
pyautogui.press('enter') # To open the site