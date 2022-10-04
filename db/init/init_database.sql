create database if not exists recetario;

create table recetario.ingredientes (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(255) NOT NULL
);

create table recetario.tipos (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(255) NOT NULL
);

create table recetario.recetas (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    id_tipo int NULL,
    FOREIGN KEY (id_tipo) REFERENCES tipos(id)
);

create table recetario.ingredientes_receta (
    id_receta int NOT NULL,
    id_ingrediente int NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas(id),
    FOREIGN KEY (id_ingrediente) REFERENCES ingredientes(id)
);

create table recetario.instrucciones (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    instruccion varchar(255) NOT NULL,
    intruccion_anterior int NULL,
    FOREIGN KEY (intruccion_anterior) REFERENCES instrucciones(id)
);