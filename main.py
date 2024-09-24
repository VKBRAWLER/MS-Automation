import json
import automated as auto

# Read the data from the JSON file
with open('mouse.json', 'r') as f:
    data = json.load(f)

# Convert lists back to tuples
account_location = [tuple(lst) for lst in data["account_location"]]
tab_location = [tuple(lst) for lst in data["tab_location"]]

auto.open_ms()
auto.full_screen()
auto.scroll_down()
auto.open_all_accounts(account_location)

for i in range(2): # 2 times for 8 accounts ( 4 accounts per time )
  auto.position_tabs()
  auto.search_tabs(tab_location, 1)
  auto.exit_tabs()

auto.shutdown()