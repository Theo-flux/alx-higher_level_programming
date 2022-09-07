-- Create database `hbtn_0d_usa` and the table `cities` on your mysql server
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
state_id INT NOT NULL FOREGIN KEY REFERENCES states(id),
name VARCHAR(256) NOT NULL
);
