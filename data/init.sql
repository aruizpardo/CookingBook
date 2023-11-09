-- Crear una tabla de tipo de recetas
DROP TABLE IF EXISTS Tipo
CREATE TABLE Tipo (
    TipoID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
);

-- Crear una tabla para donde cocinar la receta
DROP TABLE IF EXISTS LugaresCocina
CREATE TABLE LugaresCocina (
    LugarCocinaID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL
);

-- Crear una tabla para las recetas
DROP TABLE IF EXISTS Recetas
CREATE TABLE Recetas (
    RecetaID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Descripcion TEXT,
    TiempoPreparacion INTEGER,
    TipoID INTEGER,
    Porciones INTEGER,
    LugarCocinaID INTEGER,
    FOREIGN KEY (LugarCocinaID) REFERENCES LugaresCocina(LugarCocinaID),
    FOREIGN KEY (TipoID) REFERENCES Tipo(TipoID)
);

-- Crear una tabla para los ingredientes
DROP TABLE IF EXISTS Ingredientes
CREATE TABLE Ingredientes (
    IngredienteID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL
);

-- Crear una tabla para la relación entre recetas e ingredientes
DROP TABLE IF EXISTS RecetaIngredientes
CREATE TABLE RecetaIngredientes (
    RecetaID INTEGER,
    IngredienteID INTEGER,
    Cantidad TEXT,
    FOREIGN KEY (RecetaID) REFERENCES Recetas(RecetaID),
    FOREIGN KEY (IngredienteID) REFERENCES Ingredientes(IngredienteID)
);

-- Crear una tabla para las instrucciones de preparación
DROP TABLE IF EXISTS Instrucciones
CREATE TABLE Instrucciones (
    InstruccionID INTEGER PRIMARY KEY,
    RecetaID INTEGER,
    Paso INTEGER,
    Descripcion TEXT,
    FOREIGN KEY (RecetaID) REFERENCES Recetas(RecetaID)
);