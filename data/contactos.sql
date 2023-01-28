create database flaskcontacts

create table contacts (
    id int auto_increment primary key not null,
    fullname varchar(255) not null,
    phone varchar(255) not null,
    email varchar(255) not null
);