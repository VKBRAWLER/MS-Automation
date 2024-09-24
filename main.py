from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time
import json
import random
import string
import os
import pygetwindow as gw

mouse = MouseController()
keyboard = KeyboardController()

def load_json(file_path):
  with open(file_path, 'r') as file:
    data = json.load(file)
  return data

def position_tabs():
  keyboard.press(Key.cmd)
  time.sleep(0.5)
  keyboard.press(Key.up)
  keyboard.release(Key.up)
  time.sleep(0.5)
  keyboard.press(Key.left)
  keyboard.release(Key.left)
  time.sleep(0.5)
  keyboard.release(Key.cmd)
  time.sleep(0.5)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  time.sleep(0.5)
  time.sleep(0.5)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  time.sleep(0.5)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  time.sleep(0.5)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  time.sleep(0.5)

def exit_tabs():
  keyboard.press(Key.ctrl)
  time.sleep(0.5)
  keyboard.press('w')
  keyboard.release('w')
  time.sleep(0.5)
  keyboard.press('w')
  keyboard.release('w')
  time.sleep(0.5)
  keyboard.press('w')
  keyboard.release('w')
  time.sleep(0.5)
  keyboard.press('w')
  keyboard.release('w')
  time.sleep(0.5)
  keyboard.release(Key.ctrl)
  time.sleep(0.5)
  
account_location = [(1094, 947), (1096, 836), (1097, 723), (1094, 614), (1097, 500), (1098, 388), (1096, 275)]
exit_location = [(933, 14), (1885, 15), (1892, 545), (942, 541)]
tab_location = [(323, 58), (1296, 62), (348, 577), (1330, 573)]
json_data = load_json('./mouse.json')

# start here
time.sleep(2)

# Path to the application executable
# open ms
mouse.position = (1110, 1054)
time.sleep(1)
mouse.click(Button.left)

# full screen ( make sure the browser opens in minimized mode )
keyboard.press(Key.cmd)
time.sleep(0.5)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.release(Key.cmd)
time.sleep(0.5)

# Scroll down
mouse.position = (1621, 521) # click on the browser
time.sleep(0.5)
mouse.click(Button.left)
time.sleep(0.5)
mouse.scroll(0, -10)
time.sleep(0.5)

# Save the window to a variable
personal = gw.getWindowsWithTitle('Edge')[0]

# OPEN ALL ACCOUNTS
for i in account_location:
  mouse.position = i
  time.sleep(1)
  mouse.click(Button.left)
  time.sleep(2)
  personal.activate()

for i in range(2): # 2 times for 8 accounts ( 4 accounts per time )
  position_tabs()
  search_count = 1
  for i in range(search_count):
    for location in tab_location:
      mouse.position = location
      time.sleep(0.5)
      mouse.click(Button.left)
      time.sleep(0.5)
      random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
      keyboard.type(random_string)
      time.sleep(0.5)
      keyboard.press(Key.enter)
      keyboard.release(Key.enter)
  exit_tabs()

time.sleep(1)
# good night

# os.system('shutdown -s')  