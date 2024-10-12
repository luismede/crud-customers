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

    registro_clientes = int(input("\nO que você deseja fazer? (1 ou 2): "))

    while registro_clientes not in [1,2]:
      registro_clientes = int(input(Fore.RED, Style.BRIGHT + "Tente Novamente! (1 ou 2): " + Style.RESET_ALL))
      
    if registro_clientes == 1:
      clientes_registrados = 0
      while True:
        name = input("\nDigite o nome do novo cliente a ser registrado: ")
        cpf = input("Digite o CPF do novo cliente a ser registrado: ")

        
        while not validador_cpf.validate(cpf):
            print(Fore.RED, Style.BRIGHT + "\nCPF Inválido! Informe um CPF valido." + Style.RESET_ALL)
            cpf = input("\nDigite o CPF do novo cliente a ser registrado: ")

        
        create_customer(name,cpf)
        clientes_registrados += 1
        print(Fore.GREEN, Style.BRIGHT + "\nCliente registrado. Para sair pressione CTRL+C" + Style.RESET_ALL)

        
        if clientes_registrados >= 5:
          exit = int(input("\nDeseja registrar mais clientes? (1 - SIM | 2 - NÃO): "))
          while exit not in[1, 2]:
            print(Fore.RED, Style.BRIGHT + "\nOpção inválida! Use 1 ou 2."  + Style.RESET_ALL)
            registrar = input("\nDeseja registrar mais clientes? (1 - SIM | 2 - NÃO): ")
          if registrar == 1:
            continue
          else:
            print("Encerrando o Software...")
            break
    else:
        name = input("\nDigite o nome do novo cliente a ser registrado: ")
        cpf = input("Digite o CPF do novo cliente a ser registrado: ")
        while not validador_cpf.validate(cpf):
            print(Fore.RED, Style.BRIGHT + "\nCPF Inválido! Informe um CPF valido." + Style.RESET_ALL)
            cpf = input("Digite o CPF do novo cliente a ser registrado: ")
        create_customer(name,cpf)
        
        print(Fore.GREEN, Style.BRIGHT + "\nCliente registrado." + Style.RESET_ALL)
        break

if __name__ == "__main__":
  createCustomers()