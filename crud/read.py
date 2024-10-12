from db.connection import read_customer
from colorama import init, Fore, Style

init()

def readCustomers():
  print(Fore.GREEN + "\nTabela de Clientes: " + Style.RESET_ALL)
  read_customer()

if __name__ == "__main__":
  readCustomers()