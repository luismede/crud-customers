from crud.create import createCustomers
from crud.read import readCustomers
from crud.delete import deleteCustomers
from crud.update import updateCustomersCPF, updateCustomersName

from colorama import init, Fore, Style

init()

ADD_CUSTOMERS = 1
VIEW_CUSTOMERS = 2
DELETE_CUSTOMERS = 3
UPDATE_CPF = 4
UPDATE_NAME = 5

def menu():
  print(f"\n{"-+-+"*5} CRUD Software {"-+-+"*5}")
  print("""
        1 - Adicionar novos clientes
        2 - Visualizar tabela de clientes
        3 - Deletar clientes
        4 - Atualizar CPF
        5 - Atualizar nome
  """)
  try:
    return int(input("O que você deseja utilizar? "))
  except ValueError:
    print(Fore.RED + "\nEntrada inválida. Por favor, insira um número." + Style.RESET_ALL)
    return None

def main():
  while True:
    input_user = menu()
    
    if input_user not in [1,2,3,4,5]:
      print(Fore.RED + "\nOpção Inválida..." + Style.RESET_ALL)
      continue

    if input_user == ADD_CUSTOMERS:
      createCustomers()
    elif input_user == VIEW_CUSTOMERS:
      readCustomers()
    elif input_user == DELETE_CUSTOMERS:
      deleteCustomers()
    elif input_user == UPDATE_CPF:
      updateCustomersCPF()
    elif input_user == UPDATE_NAME:
      updateCustomersName()
      
if __name__ == "__main__":
  main()