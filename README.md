![screenshots](https://github.com/user-attachments/assets/c612fc4e-9da2-4f14-ac6c-fd5fd8d93d3e)

---

# Documentação da Aplicação
![GitHub License](https://img.shields.io/github/license/luismede/crud-customers)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/luismede/crud-customers)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mysql-connector-python)
![PyPI - Downloads](https://img.shields.io/pypi/dd/mysql-connector-python)




### Clonando o Repositório

Primeiro, você precisa clonar o repositório do GitHub para a sua máquina local. Abra o terminal e execute o seguinte comando:

```bash
git clone https://github.com/luismede/crud-customers.git
```

---

### Instalando Dependências

A aplicação utiliza um arquivo `requirements.txt` para listar as dependências. Para instalá-las, siga os passos abaixo:

1. Certifique-se de que você tem o **Python 3.8+** e o **pip** instalados.
   
2. Crie um ambiente virtual (opcional, mas recomendado):
   
   ```bash
   python -m venv .venv
   ```

3. Ative o ambiente virtual:

   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - No Linux/MacOS:
     ```bash
     source .venv/bin/activate
     ```

4. Instale as dependências listadas no `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

---

### Configurando o Banco de Dados MySQL

A aplicação requer um banco de dados MySQL para armazenar os clientes. Siga os passos abaixo para configurar o banco de dados:

1. **Instale o MySQL**:
   
   Se o MySQL não estiver instalado na sua máquina, siga as instruções de instalação para o seu sistema operacional [aqui](https://dev.mysql.com/downloads/installer/).

2. **Acesse o MySQL**:

   Use o seguinte comando para acessar o MySQL com seu usuário root (ou qualquer outro usuário com permissões adequadas):

   ```bash
   mysql -u root -p
   ```

3. **Crie o banco de dados**:

   Crie um banco de dados para a aplicação (substitua `table_clients` pelo nome desejado):

   ```sql
   CREATE DATABASE table_clients;
   ```

4. **Selecione o banco de dados**:

   ```sql
   USE table_clients;
   ```

5. **Crie a tabela `customers`**:

   Agora, crie a tabela `customers` com três colunas: `id`, `name` e `cpf`:

   ```sql
   CREATE TABLE customers (
       id SERIAL AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       cpf VARCHAR(11) NOT NULL,
       number_phone VARCHAR(15) NOT NULL,
       cep VARCHAR(9) NOT NULL,
       address VARCHAR(100) NOT NULL,
       city VARCHAR(100) NOT NULL,
       uf VARCHAR(3) NOT NULL
      
   );
   ```

   Essa tabela possui uma coluna `id` que é a chave primária e auto-incrementada, uma coluna `name` para o nome do cliente, e uma coluna `cpf` para o CPF (formato brasileiro, 11 caracteres), uma coluna `number_phone` para o telefone do cliente, uma coluna `cep`para o CEP do cliente, `addres` para o lologradouro do cliente, uma coluna `city` para a cidade em que o cliente mora e uma coluna `uf` para a UF do cliente.

---

### Executando a Aplicação

1. Certifique-se de que o banco de dados MySQL está rodando e que a tabela `customers` foi criada corretamente.
   
2. Edite as configurações de conexão com o banco de dados no código da aplicação, se necessário. Abra o arquivo onde a conexão MySQL(db.connection.py) está configurada e ajuste as credenciais:

   ```python
   engine = create_engine('mysql+pymysql://root:root@localhost:3307/table_clients')
   ```

   Substitua `root` e `root` pelas suas credenciais de banco de dados, e `table_clients` pelo nome do banco de dados que você criou.

3. Execute o script Python:

   ```bash
   python Main.py
   ```

---

### Requisitos

- Python 3.8 ou superior
- MySQL
- Bibliotecas listadas no `requirements.txt`

---

### Contribuições

Sinta-se à vontade para fazer contribuições! Basta abrir uma **issue** ou enviar um **pull request**.

