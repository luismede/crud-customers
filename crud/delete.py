from db.connection import delete_customer
from colorama import init, Fore, Style

init()

def deleteCustomers():
    try:
        while True:
            id_customer = int(input("\nDigite o ID do cliente que você deseja deletar: "))
            
            confirmacao = input(Fore.YELLOW + f"Tem certeza que deseja deletar o cliente com ID {id_customer}? (s/n): " + Style.RESET_ALL).lower()
            if confirmacao.lower() == 's':
                delete_customer(id_customer)
            else:
                print(Fore.BLUE + "\nAção cancelada." + Style.RESET_ALL)
            break
    except ValueError:
        print(Fore.RED + "\nErro: O ID deve ser um número inteiro válido." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"\nErro ao deletar o cliente: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    deleteCustomers()
