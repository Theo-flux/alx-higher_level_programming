-- Creates the database `hbtn_0c_0` and the user `user_0d_2`.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT PRIVILEGE ON *.* TO 'user_0d_2'@'localhost';
