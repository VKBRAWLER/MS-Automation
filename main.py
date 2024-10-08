import json
import automated as auto
import random_search as rs
# Read the data from the JSON file
with open('mouse.json', 'r') as f:
  data = json.load(f)

# Variables
count = 10
account_gap = 1
time_gap = 5

# Convert lists back to tuples
account_location = [tuple(lst) for lst in data["account_location"]]
search_bar_location = tuple(data["search_bar_location"])

auto.open_ms()
auto.full_screen_toggle()
auto.scroll_down()
auto.open_all_accounts(account_location)
auto.full_screen_toggle()
word_list = rs.get_search(count)
for i in range(len(account_location)+1): # each account separately
  auto.maximize()
  auto.search_tabs(word_list, search_bar_location, time_gap)
  auto.close_tab(account_gap)

auto.shutdown()