from DB.conexion import get_connection
from objetos.prestamoObj import Prestamo

def hacerPrestamo(prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "INSERT INTO `prestamo` (`id_prestamo`, `rut`, `id_ejemplar`, `fecha_prestamo`, `fecha_devolucion`, `estado`) VALUES (%s, %s, %s, %s, %s,'no terminado');"
    valores = (prestamo.getId_prestamo(),prestamo.getRut(),prestamo.getId_ejemplar(),prestamo.getFecha_prestamo(),prestamo.getFecha_devolucion())
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def cantidadPrestamo(rut):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT COUNT(*) AS total_prestamos FROM prestamo WHERE rut = %s;"
    valores = (rut,)
    cursor.execute(consulta, valores)
    resultado = cursor.fetchone()
    total_prestamos = resultado[0]
    cursor.close()
    conexion.close()
    
    return total_prestamos



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

def mostrarTodosPrestamos():
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT p.fecha_prestamo, p.fecha_devolucion, u.nombre, u.apellido, l.titulo, p.estado FROM prestamo p INNER JOIN usuario u ON p.rut = u.rut INNER JOIN ejemplar e ON p.id_ejemplar = e.id_ejemplar INNER JOIN libro l ON e.id_libro = l.id_libro;"
    cursor.execute(consulta)

    prestamos = []
    for row in cursor:
        fecha_prestamo = row[0]
        fecha_devolucion = row[1]
        nombre = row[2]
        apellido = row[3]
        titulo = row[4]
        estado = row[5]
        
        prestamo = Prestamo(None, None, None, fecha_prestamo, fecha_devolucion, estado)
        prestamo.setNombre(nombre)
        prestamo.setApellido(apellido)
        prestamo.setTitulo(titulo)
        prestamos.append(prestamo)

    conexion.close()

    return prestamos

def Buscar_Prestamo(where):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT p.id_prestamo, p.rut, p.id_ejemplar, p.fecha_prestamo, p.fecha_devolucion, u.nombre, u.apellido, l.titulo, p.estado FROM prestamo p INNER JOIN usuario u ON p.rut = u.rut INNER JOIN ejemplar e ON p.id_ejemplar = e.id_ejemplar INNER JOIN libro l ON e.id_libro = l.id_libro WHERE p.rut = "+ str(where) +";"
    cursor.execute(consulta)

    prestamos = []
    for row in cursor:
        id_prestamo = row[0]
        rut = row[1]
        id_ejemplar = row[2]
        fecha_prestamo = row[3]
        fecha_devolucion = row[4]
        nombre = row[5]
        apellido = row[6]
        titulo = row[7]
        estado = row[8]
        
        prestamo = Prestamo(id_prestamo, rut, id_ejemplar, fecha_prestamo, fecha_devolucion,estado)
        prestamo.setNombre(nombre)
        prestamo.setApellido(apellido)
        prestamo.setTitulo(titulo)
        prestamos.append(prestamo)

    conexion.close()

    return prestamos

def TerminarPrestamo(id_prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "UPDATE `prestamo` SET `estado` = 'terminado' WHERE `prestamo`.`id_prestamo` = %s;"
    valores = (id_prestamo,)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()


def UpPrestamo(id_prestamo,valor,cambio):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "UPDATE `prestamo` SET "+ cambio +" = %s WHERE `prestamo`.`id_prestamo` = %s;"
    valores = (valor,id_prestamo,)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()



