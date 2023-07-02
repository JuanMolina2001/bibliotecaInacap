from DB.conexion import get_connection
from objetos.prestamoObj import Prestamo

def hacerPrestamo(prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "INSERT INTO `prestamo` (`id_prestamo`, `rut`, `id_ejemplar`, `fecha_prestamo`, `fecha_devolucion`) VALUES (%s, %s, %s, %s, %s);"
    valores = (prestamo.getId_prestamo(),prestamo.getRut(),prestamo.getId_ejemplar(),prestamo.getFecha_prestamo(),prestamo.getFecha_devolucion())
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()





def seleccionarEjemplar(id_libro):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT id_ejemplar FROM ejemplar WHERE id_libro = %s AND estado = 'Disponible'"
    valores = (id_libro,)
    cursor.execute(consulta, valores)

    id_ejemplar = None

    for row in cursor:
        id_ejemplar = row[0]
        break
    cursor.fetchall()
    cursor.close()
    conexion.close()

    if id_ejemplar is None:
        print("No hay ejemplares disponibles")
        return 
    return id_ejemplar
