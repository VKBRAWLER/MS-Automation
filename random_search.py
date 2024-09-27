import os
from dotenv import load_dotenv

def get_existing_file_path(base_path):
  counter = 1
  while not os.path.exists(base_path):
    base_path = base_path.replace(f"_{counter}.txt", f"_{counter + 1}.txt")
    counter += 1
  return base_path

def get_search(elements=10, safe=False):
  load_dotenv()
  file_path = os.getenv('TXT_FILE_NAME')
  file_path = get_existing_file_path(file_path)
  with open(file_path, 'r') as file:
    lines = file.readlines()
  list = lines[:elements]
  remain = lines[elements:]
  if not remain:
    os.remove(file_path)
  elif not safe:
    with open(file_path, 'w') as file:
      file.writelines(remain)
  return [element.strip() for element in list]

# print(get_search(5, True))