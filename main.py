import json
import automated as auto
import random_search as rs
import subprocess
# Read the data from the JSON file
with open('data.json', 'r') as f:
  data = json.load(f)

# Variables
profile = data["profile"]
search_bar_location = tuple(data["search_bar_location"])
devtool_location = tuple(data["devtool_location"])
count = 30
account_gap = 1
time_gap = 5
mainapp = r'c:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --profile-directory='

for i in profile:
  subprocess.Popen(mainapp + '"' + i + '"')
  auto.maximize()
  auto.collect_rewards(devtool_location)
  
  word_list = rs.get_search(count)
  auto.search_tabs(word_list, search_bar_location, time_gap)
  auto.close_tab(account_gap)

auto.shutdown()