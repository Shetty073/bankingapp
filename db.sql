CREATE DATABASE IF NOT EXISTS banking_db;
USE banking_db;
CREATE TABLE users (cif INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(512), balance DECIMAL, username VARCHAR(256), password VARCHAR(256));
CREATE TABLE transactions (id INT PRIMARY KEY AUTO_INCREMENT, user_cif INT, action VARCHAR(150), amount DECIMAL, balance_before DECIMAL, balance_after DECIMAL);
INSERT INTO users (name, balance, username, password) VALUES ("Ashish", 100000, "ashish", "ashish");
SELECT * FROM users;