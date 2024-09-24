import json

# Your new list of tuples
new_tab_location = [(323, 58), (1296, 62), (348, 577), (1330, 573)]

# Convert tuples to lists
new_tab_location_list = [list(t) for t in new_tab_location]

# Read, update, and write the JSON file in one go
with open('mouse.json', 'r+') as f:
  data = json.load(f)
  data['tab_location'] = new_tab_location_list
  f.seek(0)
  json.dump(data, f, indent=4)
  f.truncate()
