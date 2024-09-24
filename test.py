from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time
import json
import os
import pygetwindow as gw
time.sleep(2)
mouse = MouseController()
keyboard = KeyboardController()
# # Path to the application executable
# app_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
keyboard.press('w')
keyboard.release('w')
# # Open the application
# os.startfile(app_path)
# Focus on the already open application window
window = gw.getWindowsWithTitle('Edge')
for i in window:
  if i.title.find('Personal') != -1:
    i.activate()
    break