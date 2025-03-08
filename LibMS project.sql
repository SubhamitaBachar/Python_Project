create schema LMS;
use lms;
create table lms.LIBRARIAN(
LID VARCHAR(10) PRIMARY KEY,
NAME VARCHAR(30) NOT NULL,
CONTACT CHAR(10),
EMAIL VARCHAR(40));

CREATE TABLE LMS.STUDENTS(
SID VARCHAR(10) PRIMARY KEY,
SNAME VARCHAR(30),
GENDER VARCHAR(5),
AGE SMALLINT,
CONTACT CHAR(10),
DEPT VARCHAR(10),
YEAR VARCHAR(5));


create table lms.BOOKS(
BID VARCHAR(10) PRIMARY KEY,
BNAME VARCHAR(50),
AUTHOR_NAME VARCHAR(30),
AVAILABILITY varchar(5),
COPIES CHAR(3));

create table issue_book(
sid varchar(10),
sname varchar(30),
dept varchar(10),
year varchar(5),
bid varchar(10),
bname varchar(50),
author_name varchar(50),
issue_date date);

create table submit_book(
sid varchar(10),
sname varchar(30),
dept varchar(10),
year varchar(5),
bid varchar(10),
bname varchar(50),
author_name varchar(50),
deposit_date date);


INSERT INTO LIBRARIAN VALUES ('L001','SATISH KUMAR',9876543216,'KUMARSATISH001@GMAIL.COM');
INSERT INTO LIBRARIAN VALUES ('L002','SHAKTI ROY',9845543216,'ROYSHAKTI002@GMAIL.COM');
INSERT INTO LIBRARIAN VALUES ('L003','RAMESH DAS',9872843216,'DASRAMESH003@GMAIL.COM');


insert into students VALUES ('S001','VIRAT ROY','M',23,9876512345,'DEE','4TH');
insert into students VALUES ('S002','RITU PAUL','F',23,9776512345,'DEE','3RD');
insert into students VALUES ('S003','JENNY CHOUHAN','F',21,9876712345,'DEE','2ND');
insert into students VALUES ('S004','VAIBHAV PAWAR','M',19,9861212345,'DEE','1ST');
insert into students VALUES ('S005','VAISHNAVI MEHTA','F',23,9876712345,'DME','4TH');
insert into students VALUES ('S006','ABHISHEK SEN','M',22,9876516345,'DME','3RD');
insert into students VALUES ('S007','RITWIK PALSE','M',21,8876512345,'DME','2ND');
insert into students VALUES ('S008','SOURAV SEN','M',20,9976512345,'DME','1ST');
insert into students VALUES ('S009','MADHU ROY','F',22,7776512345,'DCSE','4TH');
insert into students VALUES ('S010','VAIBHAV PALSE','M',21,8696512345,'DCSE','3RD');
insert into students VALUES ('S011','ANITA MAITY','F',20,6126512345,'DCSE','2ND');
insert into students VALUES ('S012','MOUSUMI BERA','F',19,6006512345,'DCSE','1ST');
insert into students VALUES ('S013','ANIMESH JADHAV','M',22,7006512345,'DMET','4TH');
insert into students VALUES ('S014','AKIRA PANDIT','F',21,9806512345,'DMET','3RD');
insert into students VALUES ('S015','SAIKAT BISWAS','M',20,9896512345,'DMET','2ND');
insert into students VALUES ('S016','TRISHA PAUL','F',19,9876672345,'DMET','1ST');

insert into books values('B001','BASIC ELECTRONICS','B L THEREJA','YES',5);
insert into books values('B002','MODERN POWER SYSTEM ANALYSIS','KOTHARI NAGRATH','YES',2);
insert into books values('B003','ELECTRICAL MACHINES','MEHTA & MEHTA','YES',3);
insert into books values('B004','ENGINEERING MECHANICS','RS KHUMRI','YES',1);
insert into books values('B005','BASICS AND APPLIED THERMODYNAMICS','P K NAG','YES',7);
insert into books values('B006','MACHINE DRAWING','P S GILL','YES',5);
insert into books values('B007','DATA STRUCTURES','RS SALARIA','YES',8);
insert into books values('B008','OBJECT ORIENTED PROGRAMMING IN C++ AND JAVA','D. SAMANTHA','YES',10);
insert into books values('B009','METALLURGICAL THERMODYNAMICS','SK DUTTA','YES',11);
insert into books values('B010','SOLID STATE PHASE TRANSFORMATION','V RAGHAVAN','YES',15);


select * from submit_book;
truncate books;