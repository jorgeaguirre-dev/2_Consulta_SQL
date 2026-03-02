# 2 - Consulta SQL

## Descripción
En este proyecto, se provee una base de datos con dos tablas: `Amigo` y `Miembro`, y con tablas adicionales como `Persona` y `Grupo`.
La tabla `Amigo` contiene información sobre las amistades entre personas, mientras que la tabla `Miembro` contiene información sobre los grupos a los que pertenecen esas personas.

La consulta SQL debe dar el nombre de cada persona junto con el nombre del grupo al que pertenece, pero solo si todos sus amigos también pertenecen a ese mismo grupo.

### Modelo Entidad Relación
![DER](img/diagrama.png)

## Ejecución Rápida
- Al tener Python instalado, es posible clonar y ver el resultado del proyecto con un solo comando:

```Bash
python main.py
```

Este script inicializa una base de datos en memoria (o archivo), carga el esquema, inserta 20 registros de prueba y ejecuta la consulta SQL.

- Para probar directamente la consulta SQL contra la DB data.db usar:
```Bash
sqlite3 data/data.db < sql/consulta.sql
```

## Ejemplo de Ejecución y Resultado
### Tabla Amigo

![Amigo](img/amigo.png)

### Tabla Miembro

![Miembro](img/miembro.png)

### Resultado Esperado

![Resultado](img/resultado.png)



