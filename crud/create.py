from db.connection import create_customer
from validate_docbr import CPF
from colorama import init, Fore, Style

init()

validador_cpf = CPF()

def createCustomers():
    while True:
            print(Fore.GREEN + "\nRegistro de Clientes" + Style.RESET_ALL)
            name = input("\nDigite o nome do(a) cliente: ")
            cpf = input("CPF: ")
            number = input("Telefone: ")
            cep = input("CEP: ")
            address = input("Logradouro: ")
            city = input("Cidade: ")
            uf =input("UF: ")

            while not validador_cpf.validate(cpf):
                print(Fore.RED + "CPF inválido! Informe um CPF válido." + Style.RESET_ALL)
                cpf = input("Digite o CPF do(a) novo(a) cliente a ser registrado: ")

            create_customer(name, cpf, number, cep, address, city, uf)
            print(Fore.GREEN + f"Cliente {name} registrado(a) com sucesso!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    createCustomers()
