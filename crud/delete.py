from db.connection import delete_customer
from colorama import init, Fore, Style

init()

def deleteCustomers():
    try:
        while True:
            cpf_customer = input("\nDigite o CPF do cliente que você deseja deletar: ")
            
            confirmacao = input(Fore.YELLOW + f"Tem certeza que deseja deletar o cliente com CPF {cpf_customer}? (s/n): " + Style.RESET_ALL).lower()
            if confirmacao.lower() == 's':
                delete_customer(cpf_customer)
            else:
                print(Fore.BLUE + "\nAção cancelada." + Style.RESET_ALL)
            break
    except Exception as e:
        print(Fore.RED + f"\nErro ao deletar o cliente: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    deleteCustomers()
