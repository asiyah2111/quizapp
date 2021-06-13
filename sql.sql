CREATE DATABASE 7pmexamdb;
CREATE TABLE user_profile(uid INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50) UNIQUE, pwd VARCHAR(50), NAME VARCHAR(50),email VARCHAR(50),role VARCHAR(50));
CREATE TABLE technology(tid INT PRIMARY key AUTO_INCREMENT,tname VARCHAR(100) UNIQUE);
CREATE TABLE questions(qid INT PRIMARY KEY AUTO_INCREMENT, question VARCHAR(200) UNIQUE, opta VARCHAR(50),optb VARCHAR(50),optc VARCHAR(50),optd VARCHAR(50),correct VARCHAR(20),techid INT,FOREIGN KEY(techid) REFERENCES technology(tid));
CREATE TABLE result(rid INT PRIMARY KEY AUTO_INCREMENT,userid INT,techid INT,marks FLOAT,resdate DATE,sts INT,FOREIGN KEY(userid) REFERENCES user_profile(uid),
FOREIGN KEY(techid) REFERENCES technology(tid));
INSERT INTO user_profile VALUES(1,'admin123','1234','Munawwar Ali','munawwarali@gmail.com','admin');