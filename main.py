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

# Read the data from the JSON file
with open('mouse.json', 'r') as f:
    data = json.load(f)

# Convert lists back to tuples
account_location = [tuple(lst) for lst in data["account_location"]]
tab_location = [tuple(lst) for lst in data["tab_location"]]

def position_tabs():
  keyboard.press(Key.cmd)
  time.sleep(0.5)
  keyboard.tap(Key.up)
  time.sleep(0.5)
  keyboard.tap(Key.left)
  time.sleep(0.5)
  keyboard.release(Key.cmd)
  time.sleep(0.5)
  keyboard.tap(Key.enter)
  time.sleep(0.5)
  time.sleep(0.5)
  keyboard.tap(Key.enter)
  time.sleep(0.5)
  keyboard.tap(Key.enter)
  time.sleep(0.5)
  keyboard.tap(Key.enter)
  time.sleep(0.5)

def exit_tabs():
  keyboard.press(Key.ctrl)
  time.sleep(0.5)
  keyboard.tap('w')
  time.sleep(0.5)
  keyboard.tap('w')
  time.sleep(0.5)
  keyboard.tap('w')
  time.sleep(0.5)
  keyboard.tap('w')
  time.sleep(0.5)
  keyboard.release(Key.ctrl)
  time.sleep(0.5)

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
keyboard.tap(Key.up)
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
      keyboard.tap(Key.enter)
  exit_tabs()

time.sleep(1)
# good night
# os.system('shutdown -s')