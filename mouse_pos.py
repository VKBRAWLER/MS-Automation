from pynput import mouse, keyboard

def on_click(x, y, button, pressed):
  if pressed:
    print(f"Mouse clicked at ({x}, {y})")

def on_press(key):
  try:
    if key == keyboard.Key.esc:
      # Stop the mouse listener
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