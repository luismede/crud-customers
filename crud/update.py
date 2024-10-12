from db.connection import update_cpf, update_name
from colorama import init, Fore, Style

init()

def updateCustomersName():
  while True:
    print(Fore.GREEN + "\nAtualizar nome do cliente" + Style.RESET_ALL)
    id_customer = int(input("Digite o ID do cliente que você deseja atualizar o nome: "))
    name_customer = input("Digite o novo Nome do cliente: ")
    update_name(name_customer, id_customer)
    
    print(Fore.GREEN + "\nCliente atualizado com sucesso!" + Style.RESET_ALL)
    break
    
    
def updateCustomersCPF():
  while True:
    print(Fore.GREEN + "\nAtualizar CPF do cliente" + Style.RESET_ALL)
    id_customer = int(input("Digite o ID do cliente que você deseja atualizar o CPF: "))
    cpf_customer = input("Digite o novo CPF do cliente: ")
    update_cpf(cpf_customer, id_customer)
    
    print(Fore.GREEN + "\nCliente atualizado com sucesso!" + Style.RESET_ALL)
    break
    
if __name__ == "__main__":
  updateCustomersName()
  updateCustomersCPF()