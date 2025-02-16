
CREATE DATABASE IF NOT EXISTS myflaskapp;
use myflaskapp;

CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    username varchar(255),
    password varchar(255)
);

INSERT INTO users VALUES(null, "juan", "juan@gmail.com", "juan", "123"),
    (null, "maria", "maria@gmail.com", "maria", "456");

CREATE TABLE IF NOT EXISTS products (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price FLOAT NOT NULL
);

INSERT INTO products (name, description, price)
VALUES
('Laptop', 'Laptop de gama media', 650.99),
('Smartphone', 'Smartphone Android', 299.50),
('Auriculares', 'Auriculares Bluetooth', 45.00);