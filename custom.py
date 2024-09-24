import automated as auto
import time

while (True):
  choice = (input("Enter 1 to open MS Teams\n 2 to open all accounts\n 3 to position tabs\n 4 to search tabs\n 5 to exit tabs\n 6 to exit\n"))
  if choice == "1":
    time.sleep(2)
    auto.open_ms()
  elif choice == "2":
    time.sleep(2)
    auto.open_all_accounts()
  elif choice == "3":
    time.sleep(2)
    auto.position_tabs()
  elif choice == "4":
    count = int(input("Enter the number of times you want to search: "))
    time.sleep(2)
    auto.search_tabs(count)
  elif choice == "5":
    time.sleep(2)
    auto.exit_tabs()
  else:
    break