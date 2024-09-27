import json
from pynput import mouse, keyboard

new_account_location = []

def on_click(x, y, button, pressed):
  if pressed:
    new_account_location.append((x, y))

# Stop the mouse listener
def on_press(key):
  try:
    if key == keyboard.Key.esc:
      return False
  except AttributeError:
    pass

# Set up the mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Set up the keyboard listener
with keyboard.Listener(on_press=on_press) as keyboard_listener:
  keyboard_listener.join()

# Stop the mouse listener when the keyboard listener stops
mouse_listener.stop()

# Convert tuples to lists
new_account_location_list = [list(t) for t in new_account_location]

# Read, update, and write the JSON file in one go
with open('mouse.json', 'r+') as f:
  data = json.load(f)
  data['account_location'] = new_account_location_list
  f.seek(0)
  json.dump(data, f, indent=4)
  f.truncate()
