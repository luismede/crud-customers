import tkinter as tk
from tkinter import ttk
from db.connection import read_customer
from colorama import init, Fore, Style

init()

def readCustomers():
    try:
        print(Fore.GREEN + "\nTabela de Clientes: " + Style.RESET_ALL)
        
        def populate_table():
            rows = read_customer()
            if rows: 
                for row in rows:
                    tree.insert("", "end", values=row)
            else:
                print("Nenhum dado foi retornado da tabela.")

        root = tk.Tk()
        root.title("Tabela de Clientes")
        root.geometry("900x300")

        frame = tk.Frame(root)
        frame.pack(fill="both", expand=True)

        columns = ("id", "name", "cpf", "number_phone", "cep", "address", "city", "uf")
        tree = ttk.Treeview(frame, columns=columns, show="headings")

        tree.heading("id", text="ID")
        tree.heading("name", text="Nome")
        tree.heading("cpf", text="CPF")
        tree.heading("number_phone", text="Telefone")
        tree.heading("cep", text="CEP")
        tree.heading("address", text="Logradouro")
        tree.heading("city", text="Cidade")
        tree.heading("uf", text="UF")

        tree.column("id", width=50, anchor="center")          # ID
        tree.column("name", width=150)                        # Nome
        tree.column("cpf", width=120, anchor="center")        # CPF
        tree.column("number_phone", width=120, anchor="center") # Telefone
        tree.column("cep", width=80, anchor="center")         # CEP
        tree.column("address", width=200)                     # Logradouro
        tree.column("city", width=120)                        # Cidade
        tree.column("uf", width=40, anchor="center")          # UF

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)

        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        populate_table()

        root.mainloop()

    except Exception as e:
        print(Fore.RED + f"\nErro ao ler a tabela de clientes: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    readCustomers()
