create table ingredientes (
    id INTEGER PRIMARY KEY,
    nombre varchar(255) NOT NULL UNIQUE
);

create table tipos (
    id INTEGER PRIMARY KEY,
    nombre varchar(255) NOT NULL
);

create table recetas (
    id INTEGER PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    id_tipo int NULL,
    FOREIGN KEY (id_tipo) REFERENCES tipos(id)
);

create table ingredientes_receta (
    id_receta int NOT NULL,
    id_ingrediente int NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas(id),
    FOREIGN KEY (id_ingrediente) REFERENCES ingredientes(id)
);

create table instrucciones (
    id INTEGER PRIMARY KEY,
    instruccion varchar(255) NOT NULL,
    id_receta int NOT NULL,
    intruccion_anterior int NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas(id),
    FOREIGN KEY (intruccion_anterior) REFERENCES instrucciones(id)
);