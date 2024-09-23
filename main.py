from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time
import json
import random
import string
import os

mouse = MouseController()
keyboard = KeyboardController()

def load_json(file_path):
  with open(file_path, 'r') as file:
    data = json.load(file)
  return data

def open_acc(index):
  mouse.position = account_location[0]
  time.sleep(1)
  mouse.click(Button.left)
  time.sleep(1)
  mouse.position = account_location[index]
  time.sleep(1)
  mouse.click(Button.left)
  time.sleep(1)


account_location = [ (29, 21), (160, 300), (160, 342), (160, 368)]
tab_location = [(569, 22), (1554, 16), (548, 536), (1503, 535)]

json_data = load_json('./mouse.json')

time.sleep(2)
# open ms
mouse.position = (1091, 1054)
time.sleep(1)
mouse.click(Button.left)

keyboard.press(Key.cmd)
keyboard.press(Key.up)
keyboard.release(Key.up)
keyboard.release(Key.cmd)
# OPEN ALL ACCOUNTS
open_acc(1)
open_acc(1)
open_acc(2)
# position accounts
keyboard.press(Key.cmd)
time.sleep(1)
keyboard.press(Key.up)
keyboard.release(Key.up)
time.sleep(1)
keyboard.press(Key.left)
keyboard.release(Key.left)
time.sleep(1)
keyboard.release(Key.cmd)
time.sleep(1)

keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
exit()
#   loop for search
search_count = 10

for i in range(search_count):
  for location in tab_location:
    mouse.position = location
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    keyboard.type(random_string)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

time.sleep(1)
# good night

os.system('shutdown -s')