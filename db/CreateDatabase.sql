CREATE DATABASE table_clients;
USE table_clients;
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