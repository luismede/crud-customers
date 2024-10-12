from db.connection import update_cpf, update_name
from validate_docbr import CPF
from colorama import init, Fore, Style

init()
validador_cpf = CPF()

def updateCustomersName():
    try:
        print(Fore.GREEN + "\nAtualizar nome do cliente" + Style.RESET_ALL)
        id_customer = int(input("Digite o ID do cliente que você deseja atualizar o nome: "))
        name_customer = input("Digite o novo Nome do cliente: ")

        if len(name_customer) == 0:
            print(Fore.RED + "\nNome inválido! O nome não pode estar vazio." + Style.RESET_ALL)
            return

        update_name(name_customer, id_customer)
    except Exception as e:
        print(Fore.RED + f"\nErro ao atualizar o cliente: {str(e)}" + Style.RESET_ALL)

    
def updateCustomersCPF():
    try:
        print(Fore.GREEN + "\nAtualizar CPF do cliente" + Style.RESET_ALL)
        id_customer = int(input("Digite o ID do cliente que você deseja atualizar o CPF: "))
        cpf_customer = input("Digite o novo CPF do cliente: ")

        while not validador_cpf.validate(cpf_customer):
            print(Fore.RED + "\nCPF inválido! Informe um CPF válido." + Style.RESET_ALL)
            cpf_customer = input("Digite o novo CPF do cliente: ")

        update_cpf(cpf_customer, id_customer)
    except Exception as e:
        print(Fore.RED + f"\nErro ao atualizar o CPF do cliente: {str(e)}" + Style.RESET_ALL)

    
if __name__ == "__main__":
    updateCustomersName()
    updateCustomersCPF()
