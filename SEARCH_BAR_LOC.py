import json
from pynput import mouse

new_search_bar_location = None

def on_click(x, y, button, pressed):
  global new_search_bar_location
  if pressed:
    new_search_bar_location = (x, y)

# Set up the mouse listener
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Stop the mouse listener when the location is set
while new_search_bar_location is None:
  pass

mouse_listener.stop()

# Read, update, and write the JSON file in one go
with open('mouse.json', 'r+') as f:
  data = json.load(f)
  data['search_bar_location'] = new_search_bar_location
  f.seek(0)
  json.dump(data, f, indent=4)
  f.truncate()
