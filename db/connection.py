import mysql.connector
import pandas as pd

from mysql.connector import Error
from colorama import Style, Fore
from sqlalchemy import create_engine

def create_connection():
  try:
    connection = mysql.connector.connect(
      host="localhost",
      user="root",
      password="passw0rd",
      database="table_clients"
    )
    if connection.is_connected():
      return connection
  except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
    return None

def close_connection(connection):
  if connection.is_connected():
    connection.close()
    
# Adicionando Clientes ao MYSQLs
def create_customer(name, cpf, number, cep, address, city, uf):
  connection = create_connection()
  if connection:
    cursor = connection.cursor()
    try:
        sql = "INSERT INTO customers (name, cpf, number_phone, cep, address, city, uf) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(name, cpf, number, cep, address, city, uf))
        connection.commit()
    except mysql.connector.Error as err:
        print(Fore.RED + f"Erro: {err}" + Style.RESET_ALL)
    finally:
        cursor.close()
        close_connection(connection)
  
  
# Deletando Clientes da Tabela
def delete_customer(customer_cpf):
  connection = create_connection()
  if connection:
    cursor = connection.cursor()
        
    sql_check = "SELECT * FROM table_clients.customers WHERE cpf = %s"
    val_check = (customer_cpf,)
    cursor.execute(sql_check, val_check)
    
    result = cursor.fetchall()
    
    if not result:
      print(Fore.RED + f"Cliente com CPF {customer_cpf} não encontrado." + Style.RESET_ALL)
    else:
      try:
          sql = f"DELETE FROM table_clients.customers WHERE cpf = %s;"
          val = (customer_cpf,)
          cursor.execute(sql, val)
          connection.commit()
          print(Fore.GREEN + f"Cliente com ID {customer_cpf} deletado." + Style.RESET_ALL)
      except mysql.connector.Error as err:
          print(Fore.RED + f"Erro: {err}" + Style.RESET_ALL)
      finally:
          cursor.close()
          close_connection(connection)

# Visualizando Tabela
def read_customer():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            sql = "SELECT * FROM customers"
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
        except mysql.connector.Error as err:
            print(Fore.RED + f"Erro: {err}" + Style.RESET_ALL)
            return []
        finally:
            cursor.close()
            close_connection(connection)


# Gerar arquivo .CSV
def gen_csv_file(name_file):
  engine = create_engine('mysql+pymysql://root:passw0rd@localhost/table_clients')
  try:
    sql = "SELECT * FROM customers"
    
    result_dataframe = pd.read_sql(sql, engine)
    
    if not result_dataframe.empty:
      result_dataframe.to_csv(name_file + ".csv")
      print(Fore.GREEN + "O Arquvio CSV foi gerado com sucesso." + Style.RESET_ALL)
    else:
      print(Fore.YELLOW + f"Nenhum cliente foi encontrado. O arquivo CSV não foi gerado!" + Style.RESET_ALL)
  except Exception as err:
    print(Fore.RED + f"Erro: {err}" + Style.RESET_ALL)

# Atualizando nome de clientes
def update_customer(new_number, new_cep, new_address, new_city, customer_id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
          sql = "UPDATE customers SET number, cep, address, city = %s, %s, %s, %s WHERE id = %s"
          cursor.execute(sql, (new_number, new_cep, new_address, new_city, customer_id))
          connection.commit()
          print(Fore.BLUE + f"Nome do cliente com ID {customer_id} atualizado com sucesso" + Style.RESET_ALL)
        except mysql.connector.Error as err:
          print(Fore.RED + f"Erro: {err}" + Style.RESET_ALL)
        finally:
          cursor.close()
          close_connection(connection)
  
# Pesquisar cliente po CPF
def search_customer(customer_cpf):
  connection = create_connection()
  if connection:
    cursor = connection.cursor()
        
    sql_check = "SELECT * FROM table_clients.customers WHERE cpf = %s"
    val_check = (customer_cpf,)
    cursor.execute(sql_check, val_check)
    
    result = cursor.fetchall()
    
    if not result:
      print(Fore.RED + f"Cliente com CPF {customer_cpf} não encontrado." + Style.RESET_ALL)
    else:
      try:
          sql = "SELECT * FROM customers WHERE cpf = %s"
          val = (customer_cpf,)
          cursor.execute(sql, val)
          rows = cursor.fetchall()
          return rows
      except mysql.connector.Error as err:
          print(Fore.RED + f"Erro: {err}" + Style.RESET_ALL)
          return []
      finally:
          cursor.close()
          close_connection(connection)
          
if __name__ == "__main__":
  gen_csv_file("Teste")
