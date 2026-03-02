import sqlite3
import os

def ejecutar_script_sql(cursor, ruta_archivo):
    """Lee un archivo .sql y lo ejecuta en el cursor dado."""
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            sql = f.read()
            cursor.executescript(sql)
            print(f"✔ Ejecutado: {ruta_archivo}")
    else:
        print(f"✖ Error: No se encontró {ruta_archivo}")

def poblar_datos(cursor):
    """Inserta los datos de prueba (Seed)."""
    # Personas
    personas = [
        ('Juan', 25, 'M'), ('Maria', 24, 'F'), ('Pedro', 26, 'M'),
        ('Ana', 23, 'F'), ('Luis', 28, 'M'), ('Elena', 22, 'F'), ('Santi', 30, 'M')
    ]
    cursor.executemany('INSERT INTO Persona VALUES (?,?,?)', personas)

    # Grupos
    grupos = [('Pythonistas', '2023-01-01'), ('SQL_Masters', '2023-02-01'), ('GCP_Experts', '2023-03-01')]
    cursor.executemany('INSERT INTO Grupo VALUES (?,?)', grupos)

    # Amistades (Simétricas)
    amistades = [
        ('Juan', 'Maria'), ('Maria', 'Juan'),
        ('Juan', 'Pedro'), ('Pedro', 'Juan'),
        ('Ana', 'Elena'), ('Elena', 'Ana'),
        ('Luis', 'Santi'), ('Santi', 'Luis')
    ]
    cursor.executemany('INSERT INTO Amigo VALUES (?,?)', amistades)

    # Miembros
    membresias = [
        ('Maria', 'SQL_Masters'), ('Pedro', 'SQL_Masters'), # Amigos de Juan en SQL_Masters
        ('Ana', 'Pythonistas'), ('Elena', 'Pythonistas'), ('Juan', 'Pythonistas')
    ]
    cursor.executemany('INSERT INTO Miembro VALUES (?,?)', membresias)
    print("✔ Datos de prueba insertados.")

def main():
    db_path = 'data/data.db'
    
    # Resetear DB para seed limpio
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # 1. Crear esquema desde archivo externo
        ejecutar_script_sql(cursor, 'sql/schema.sql')

        # 2. Insertar datos
        poblar_datos(cursor)
        conn.commit()

        # 3. Ejecutar y mostrar el resultado de la consulta
        with open('sql/consulta.sql', 'r', encoding='utf-8') as f:
            query = f.read()
            resultados = cursor.execute(query).fetchall()
            
            if not resultados:
                print("No se encontraron coincidencias.")
            for row in resultados:
                print(f"Persona: {row[0]} | Grupo Sugerido: {row[1]}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()