"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conn = sqlite3.connect("Base")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS persona(
        idPersona INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre TEXT(30), 
        fechaNacimiento TEXT(10), 
        dni INTEGER, 
        altura INTEGER)""")

    conn.commit()

    cursor.close()
    conn.close()



def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""

    conn = sqlite3.connect("Base")
    cursor = conn.cursor()

    cursor.execute("""DROP TABLE IF EXISTS persona""")
    conn.commit()

    cursor.close()
    conn.close()



# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
