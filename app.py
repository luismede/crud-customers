from crud.create import createCustomers
from crud.read import readCustomers
from crud.delete import deleteCustomers
from crud.update import updateCustomersCPF, updateCustomersName

from colorama import init, Fore, Style

init()

while True:
  print(f"\n{"-+-+"*5} CRUD Software {"-+-+"*5}")
  print("""
        1 - Adicionar novos clientes
        2 - Visualizar tabela de clientes
        3 - Deletar clientes
        4 - Atualizar CPF
        5 - Atualizar nome
  """)
  input_user = int(input("O que você deseja utilizar? "))
  while input_user not in [1,2,3,4,5]:
    print(Fore.RED + "\nOpção Inválida..." + Style.RESET_ALL)
    input_user = int(input("O que você deseja utilizar? "))
    
  if input_user == 1:
    createCustomers()
  elif input_user == 2:
    readCustomers()
  elif input_user == 3:
    deleteCustomers()
  elif input_user == 4:
    updateCustomersCPF()
  else:
    updateCustomersName()