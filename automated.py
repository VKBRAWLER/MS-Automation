from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time
import json
import os
import pygetwindow as gw
import random_search as rs

mouse = MouseController()
keyboard = KeyboardController()

# Read the data from the JSON file
with open('mouse.json', 'r') as f:
  data = json.load(f)

# Convert lists back to tuples
default_account_location = [tuple(lst) for lst in data["account_location"]]
default_search_bar_location = tuple(data["search_bar_location"])

def open_ms():
  time.sleep(1)
  mouse.position = (1110, 1054)
  time.sleep(0.5)
  mouse.click(Button.left)
  time.sleep(0.5)

def full_screen_toggle():
  time.sleep(0.5)
  keyboard.tap(Key.f11)
  time.sleep(0.5)

def scroll_down():
  mouse.position = (1621, 521) # click on the browser
  time.sleep(1.5)
  mouse.click(Button.left)
  time.sleep(0.5)
  mouse.scroll(0, -10)
  time.sleep(0.5)

def open_all_accounts(account_location=default_account_location):
  # Save the window to a variable
  personal = gw.getWindowsWithTitle('Edge')[0]
  for i in account_location:
    mouse.position = i
    time.sleep(0.5)
    mouse.click(Button.left)
    time.sleep(0.5)
    personal.activate() # Activate the window

def maximize():
  time.sleep(0.5)
  keyboard.press(Key.alt)
  time.sleep(0.5)
  keyboard.tap(Key.space)
  time.sleep(0.5)
  keyboard.tap('x')
  time.sleep(0.5)
  keyboard.release(Key.alt)
  time.sleep(0.5)

def search_tabs(count=10, search_bar_location=default_search_bar_location, time_gap=10):
  word_list = rs.get_search(count)
  for i in range(len(word_list)):
    mouse.position = search_bar_location
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    keyboard.type(word_list[i])
    time.sleep(1)
    keyboard.tap(Key.enter)
    time.sleep(time_gap)

def close_tab(account_gap=10):
  keyboard.press(Key.ctrl)
  time.sleep(0.5)
  keyboard.tap('w')
  time.sleep(0.5)
  keyboard.release(Key.ctrl)
  time.sleep(account_gap)

def shutdown():
  os.system('shutdown -s')