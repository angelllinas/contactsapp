-- Se crea la base de datos
CREATE SCHEMA IF NOT EXISTS `flaskcontacts` DEFAULT CHARACTER SET utf8;

-- se cambio a la base de datos
use flaskcontacts;

create table contacts (
    id int auto_increment primary key not null,
    fullname varchar(255) not null,
    phone varchar(255) not null,
    email varchar(255) not null
);
