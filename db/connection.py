import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="passw0rd",
  database="table_clients"
)

mycursor = mydb.cursor()

# Adicionando Clientes ao MYSQL

def create_customer(x, y):
  sql = "INSERT INTO customers (name, cpf) VALUES (%s, %s)"
  val = (x,y)

  mycursor.execute(sql, val)
  
  mydb.commit()
  
# Deletando Clientes da Tabela
def delete_customer(x):
  sql = f"DELETE FROM table_clients.customers WHERE id = {x};"

  mycursor.execute(sql)
  mydb.commit()

# Visualizando Tabela
def read_customer():
  sql = "SELECT * FROM customers"
  mycursor.execute(sql)
  
  resultado = mycursor.fetchall()
  i = len(resultado)
  for x in range(0, i):
    print(f"ID: {resultado[x][0]} | " + f"Nome: {resultado[x][1]:<20} | " + f"CPF: {resultado[x][2]}")

# Atualizando nome de clientes
def update_name(x:str,y:int):
  sql = f"UPDATE table_clients.customers t SET t.name = '{x}' WHERE id = {y};"

  mycursor.execute(sql)
  mydb.commit()
  
# Atualizando CPF de clientes
def update_cpf(x:str, y:int):
  sql = f"UPDATE table_clients.customers t SET t.cpf = '{x}' WHERE id = {y};"
  
  mycursor.execute(sql)
  mydb.commit()