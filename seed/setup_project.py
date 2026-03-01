import os
import sqlite3


def generar_seed_db():
    # Creación de dB y tablas, e inserción de datos de prueba
    db_path = 'data/seed.db'

    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 1. Crear Tablas
    cursor.executescript('''
        CREATE TABLE Persona (
            nombrePersona TEXT PRIMARY KEY,
            edad INTEGER,
            genero TEXT
        );
        CREATE TABLE Grupo (
            nombreGrupo TEXT PRIMARY KEY,
            fechaInicio TEXT
        );
        CREATE TABLE Miembro (
            nombrePersona TEXT,
            nombreGrupo TEXT,
            PRIMARY KEY (nombrePersona, nombreGrupo),
            FOREIGN KEY (nombrePersona) REFERENCES Persona(nombrePersona),
            FOREIGN KEY (nombreGrupo) REFERENCES Grupo(nombreGrupo)
        );
        CREATE TABLE Amigo (
            nombrePersona1 TEXT,
            nombrePersona2 TEXT,
            PRIMARY KEY (nombrePersona1, nombrePersona2),
            FOREIGN KEY (nombrePersona1) REFERENCES Persona(nombrePersona),
            FOREIGN KEY (nombrePersona2) REFERENCES Persona(nombrePersona)
        );
    ''')

    # 2. Insertar Datos de Prueba
    # Personas
    personas = [
        ('Juan', 25, 'M'), ('Maria', 24, 'F'), ('Pedro', 26, 'M'), 
        ('Ana', 23, 'F'), ('Luis', 28, 'M'), ('Elena', 22, 'F'), ('Santi', 30, 'M')
    ]
    cursor.executemany('INSERT INTO Persona VALUES (?,?,?)', personas)

    # Grupos
    grupos = [('Pythonistas', '2023-01-01'), ('SQL_Masters', '2023-02-01'), ('GCP_Experts', '2023-03-01')]
    cursor.executemany('INSERT INTO Grupo VALUES (?,?)', grupos)

    # Relaciones de Amistad (Simétricas)
    amistades = [
        ('Juan', 'Maria'), ('Maria', 'Juan'),
        ('Juan', 'Pedro'), ('Pedro', 'Juan'),
        ('Ana', 'Elena'), ('Elena', 'Ana'),
        ('Luis', 'Santi'), ('Santi', 'Luis')
    ]
    cursor.executemany('INSERT INTO Amigo VALUES (?,?)', amistades)

    # Miembros
    membresias = [
        ('Maria', 'SQL_Masters'),
        ('Pedro', 'SQL_Masters'),
        ('Ana', 'Pythonistas'),
        ('Elena', 'Pythonistas'),
        ('Juan', 'Pythonistas'),
        ('Luis', 'GCP_Experts')
    ]
    cursor.executemany('INSERT INTO Miembro VALUES (?,?)', membresias)

    conn.commit()
    conn.close()
    print(f"✔ Base de datos '{db_path}' generada con datos de prueba.")

if __name__ == "__main__":
    generar_seed_db()