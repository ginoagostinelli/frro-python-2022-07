"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    
    conn = sqlite3.connect('Base')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM persona WHERE idPersona=?', (id_persona,))
    rs = cursor.fetchone()

    cursor.close()
    conn.close()

    if rs is None:
        return False

    persona = (rs[0], rs[1], datetime.datetime.strptime( rs[2], '%Y-%m-%d %H:%M:%S'), rs[3], rs[4])

    return persona

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
