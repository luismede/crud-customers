from db.connection import create_customer
from validate_docbr import CPF
from colorama import init, Fore, Style

init()

validador_cpf = CPF()

def createCustomers():
    while True:
        print("""
        1 - Adicionar diversos clientes
        2 - Adicionar cliente único      
        """)

        try:
            registro_clientes = int(input("\nO que você deseja fazer? (1 ou 2): "))
        except ValueError:
            print(Fore.RED + "Por favor, insira um número válido." + Style.RESET_ALL)
            continue

        while registro_clientes not in [1, 2]:
            print(Fore.RED + "Tente novamente! Escolha 1 ou 2." + Style.RESET_ALL)
            registro_clientes = int(input("\nO que você deseja fazer? (1 ou 2): "))

        if registro_clientes == 1:
            clientes_registrados = 0
            while True:
                name = input("\nDigite o nome do novo cliente a ser registrado: ")
                cpf = input("Digite o CPF do novo cliente a ser registrado: ")

                while not validador_cpf.validate(cpf):
                    print(Fore.RED + "CPF inválido! Informe um CPF válido." + Style.RESET_ALL)
                    cpf = input("\nDigite o CPF do novo cliente a ser registrado: ")

                create_customer(name, cpf)
                clientes_registrados += 1
                print(Fore.GREEN + f"Cliente {name} registrado com sucesso!" + Style.RESET_ALL)

                if clientes_registrados >= 5:
                    try:
                        exit_choice = int(input("\nDeseja registrar mais clientes? (1 - SIM | 2 - NÃO): "))
                    except ValueError:
                        print(Fore.RED + "Opção inválida! Use 1 ou 2." + Style.RESET_ALL)
                        continue
                    
                    while exit_choice not in [1, 2]:
                        print(Fore.RED + "Opção inválida! Use 1 ou 2." + Style.RESET_ALL)
                        exit_choice = int(input("\nDeseja registrar mais clientes? (1 - SIM | 2 - NÃO): "))

                    if exit_choice == 2:
                        print("Encerrando o registro de múltiplos clientes...")
                        break

        elif registro_clientes == 2:
            name = input("\nDigite o nome do novo cliente a ser registrado: ")
            cpf = input("Digite o CPF do novo cliente a ser registrado: ")

            while not validador_cpf.validate(cpf):
                print(Fore.RED + "CPF inválido! Informe um CPF válido." + Style.RESET_ALL)
                cpf = input("Digite o CPF do novo cliente a ser registrado: ")

            create_customer(name, cpf)
            print(Fore.GREEN + f"Cliente {name} registrado com sucesso!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    createCustomers()
