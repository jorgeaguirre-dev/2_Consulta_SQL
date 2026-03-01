-- Definición del Esquema de Relación

CREATE TABLE Persona (
    nombrePersona TEXT PRIMARY KEY,
    edad INTEGER,
    genero TEXT
);

CREATE TABLE Grupo (
    nombreGrupo TEXT PRIMARY KEY,
    fechaInicio DATE
);

CREATE TABLE Miembro (
    nombrePersona TEXT,
    nombreGrupo TEXT,
    PRIMARY KEY (nombrePersona, nombreGrupo),
    FOREIGN KEY (nombrePersona) REFERENCES Persona(nombrePersona) ON DELETE CASCADE,
    FOREIGN KEY (nombreGrupo) REFERENCES Grupo(nombreGrupo) ON DELETE CASCADE
);

-- La relación es simétrica: si A es amigo de B, debe existir (A, B) y (B, A)
CREATE TABLE Amigo (
    nombrePersona1 TEXT,
    nombrePersona2 TEXT,
    PRIMARY KEY (nombrePersona1, nombrePersona2),
    FOREIGN KEY (nombrePersona1) REFERENCES Persona(nombrePersona) ON DELETE CASCADE,
    FOREIGN KEY (nombrePersona2) REFERENCES Persona(nombrePersona) ON DELETE CASCADE
);