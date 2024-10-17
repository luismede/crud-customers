from db.connection import update_customer
from validate_docbr import CPF
from colorama import init, Fore, Style

init()
validador_cpf = CPF()

def updateCustomers():
    try:
        print(Fore.GREEN + "\nAtualizar nome do cliente" + Style.RESET_ALL)
        id_customer = int(input("Digite o ID do(a) cliente que você deseja atualizar os dados: "))
        new_number = input("Telefone do(a) cliente: ")
        new_cep = input("CEP: ")
        new_address = input("Logradouro: ")
        new_city = input("Cidade: ")

        if id_customer == 0:
            print(Fore.RED + "\ID inválido! O ID não pode estar vazio." + Style.RESET_ALL)
            return

        update_customer(new_number, new_cep, new_address, new_city, id_customer)
    except Exception as e:
        print(Fore.RED + f"\nErro ao atualizar o(a) cliente: {str(e)}" + Style.RESET_ALL)

    
if __name__ == "__main__":
    updateCustomers()
