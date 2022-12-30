drop table if exists ingredientes;
create table ingredientes (
    id INTEGER PRIMARY KEY,
    nombre varchar(255) NOT NULL UNIQUE
);

drop table if exists tipos;
create table tipos (
    id INTEGER PRIMARY KEY,
    nombre varchar(255) NOT NULL
);

drop table if exists recetas;
create table recetas (
    id INTEGER PRIMARY KEY,
    nombre varchar(255) NOT NULL,
    id_tipo int NULL,
    FOREIGN KEY (id_tipo) REFERENCES tipos(id)
);

drop table if exists ingredientes_receta;
create table ingredientes_receta (
    id_receta int NOT NULL,
    id_ingrediente int NOT NULL,
    cantidad string NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas(id),
    FOREIGN KEY (id_ingrediente) REFERENCES ingredientes(id)
);

drop table if exists instrucciones;
create table instrucciones (
    id INTEGER PRIMARY KEY,
    instruccion varchar(255) NOT NULL,
    id_receta int NOT NULL,
    FOREIGN KEY (id_receta) REFERENCES recetas(id)
);

drop table if exists orden_instrucciones;
create table orden_instrucciones (
    id INTEGER PRIMARY KEY,
    intruccion_anterior int NULL,
    FOREIGN KEY (id) REFERENCES instrucciones(id),
    FOREIGN KEY (intruccion_anterior) REFERENCES instrucciones(id)
);