from db.connection import delete_customer
from colorama import init, Fore, Style

init()

def deleteCustomers():
  while True:
    print(Fore.GREEN + "\nDeletar Clientes" + Style.RESET_ALL)
    id_customer = int(input("Digite o ID do cliente que você deseja deletar: "))
    delete_customer(id_customer)
    
    print(Fore.GREEN + "\nCliente deletado com sucesso!" + Style.RESET_ALL)
    break
    
    
if __name__ == "__main__":
  deleteCustomers()