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
default_account_location = [tuple(lst) for lst in data["account_location"]]
default_tab_location = [tuple(lst) for lst in data["tab_location"]]

def open_ms():
  time.sleep(1)
  mouse.position = (1110, 1054)
  time.sleep(0.3)
  mouse.click(Button.left)
  time.sleep(0.3)

def full_screen():
  keyboard.press(Key.cmd)
  time.sleep(0.5)
  keyboard.tap(Key.up)
  keyboard.release(Key.cmd)
  time.sleep(0.5)

def scroll_down():
  mouse.position = (1621, 521) # click on the browser
  time.sleep(0.5)
  mouse.click(Button.left)
  time.sleep(0.5)
  mouse.scroll(0, -10)
  time.sleep(0.5)

def open_all_accounts(account_location=default_account_location):
  # Save the window to a variable
  personal = gw.getWindowsWithTitle('Edge')[0]

  for i in account_location:
    mouse.position = i
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    personal.activate() # Activate the window

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

def search_tabs(search_count=1, tab_location=default_tab_location):
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

def shutdown():
  os.system('shutdown -s')