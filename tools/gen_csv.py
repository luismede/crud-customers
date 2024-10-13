from db.connection import gen_csv_file
from colorama import Fore, Style

def genCSVfile():
  try:
    csv_file_name = input("\nDigite o nome do novo arquivo (Sem a extensão .csv): ")
    print(f"\nGerando arquivo {csv_file_name}.CSV...")
    gen_csv_file(csv_file_name)
  except Exception as e:
    print(Fore.RED + f"\nErro ao ler a tabela de clientes: {str(e)}" + Style.RESET_ALL)
    
if __name__ == "__main__":
    genCSVfile()