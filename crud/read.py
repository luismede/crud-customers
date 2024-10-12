from db.connection import read_customer
from colorama import init, Fore, Style

init()

def readCustomers():
    try:
        print(Fore.GREEN + "\nTabela de Clientes: " + Style.RESET_ALL)
        read_customer()
    except Exception as e:
        print(Fore.RED + f"\nErro ao ler a tabela de clientes: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    readCustomers()
