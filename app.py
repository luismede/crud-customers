from crud.create import createCustomers
from crud.read import readCustomers
from crud.delete import deleteCustomers
from crud.update import updateCustomers
from tools.search import searchCustomers
from tools.gen_csv import genCSVfile

from colorama import init, Fore, Style

init()

ADD_CUSTOMERS = 1
VIEW_CUSTOMERS = 2
DELETE_CUSTOMERS = 3
UPDATE_CUSTOMERS = 4
SEARCH_CUSTOMER = 5
GEN_CSV = 6

def menu():
  print(f"\n{"-+-+"*5} CRUD Software {"-+-+"*5}")
  print("""
        1 - Adicionar novos clientes
        2 - Visualizar tabela de clientes
        3 - Deletar clientes
        4 - Atualizar Cliente
        5 - Pesquisar por cliente
        6 - Gerar arquivo CSV
  """)
  try:
    return int(input("O que você deseja utilizar? "))
  except ValueError:
    print(Fore.RED + "\nEntrada inválida. Por favor, insira um número." + Style.RESET_ALL)
    return None

def main():
  while True:
    input_user = menu()
    
    if input_user not in [1,2,3,4,5,6]:
      print(Fore.RED + "\nOpção Inválida..." + Style.RESET_ALL)
      continue

    if input_user == ADD_CUSTOMERS:
      createCustomers()
    elif input_user == VIEW_CUSTOMERS:
      readCustomers()
    elif input_user == DELETE_CUSTOMERS:
      deleteCustomers()
    elif input_user == UPDATE_CUSTOMERS:
      updateCustomers()
    elif input_user == SEARCH_CUSTOMER:
      searchCustomers()
    elif input_user == GEN_CSV:
      genCSVfile()
      
if __name__ == "__main__":
  main()