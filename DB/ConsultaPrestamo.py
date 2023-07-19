from DB.conexion import get_connection
from objetos.prestamoObj import Prestamo
from datetime import datetime , timedelta, date
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

    consulta = "SELECT u.nombre, u.apellido, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.estado, COUNT(r.dias_devolucion) AS cantidad_renovacion, sum(r.dias_devolucion) AS dias_devolucion FROM prestamo p INNER JOIN usuario u ON p.rut = u.rut INNER JOIN ejemplar e ON p.id_ejemplar = e.id_ejemplar INNER JOIN libro l ON e.id_libro = l.id_libro LEFT JOIN renovacion r ON p.id_prestamo = r.id_prestamo GROUP BY p.id_prestamo;"
    cursor.execute(consulta)

    prestamos = []
    for row in cursor:
        
        
        nombre = row[0]
        apellido = row[1]
        titulo = row[2]
        fecha_prestamo = row[3]
        fecha_devolucion = row[4]
        estado = row[5]
        renovacion = row[6]
        dias_devolucion = row [7]
        if dias_devolucion is None:
            r_fecha_devolucion = 'NULL'
        else:
            r_fecha_devolucion = fecha_devolucion + timedelta(days=int(dias_devolucion)) 
        prestamo = Prestamo(None, None, None, fecha_prestamo, fecha_devolucion, estado)
        prestamo.setNombre(nombre)
        prestamo.setApellido(apellido)
        prestamo.setTitulo(titulo)
        prestamo.setTitulo(titulo)
        prestamo.setRenovacion(renovacion)
        prestamo.setR_fecha_devolucion(r_fecha_devolucion)
        prestamos.append(prestamo)

    conexion.close()

    return prestamos

def Buscar_Prestamo(where):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT p.id_prestamo, p.rut, p.id_ejemplar, p.fecha_prestamo, p.fecha_devolucion, u.nombre, u.apellido, l.titulo, p.estado, COUNT(r.dias_devolucion) AS cantidad_renovacion, sum(r.dias_devolucion) as dias_devolucion FROM prestamo p INNER JOIN usuario u ON p.rut = u.rut INNER JOIN ejemplar e ON p.id_ejemplar = e.id_ejemplar INNER JOIN libro l ON e.id_libro = l.id_libro LEFT JOIN renovacion r ON p.id_prestamo = r.id_prestamo WHERE p.rut = %s GROUP by p.id_prestamo;;"
    valores = (where,)
    cursor.execute(consulta,valores)

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
        renovacion = row[9]
        dias_devolucion = row [10]
        if dias_devolucion is None:
            r_fecha_devolucion = 'NULL'
        else:
            r_fecha_devolucion = fecha_devolucion + timedelta(days=int(dias_devolucion)) 
        
        prestamo = Prestamo(id_prestamo, rut, id_ejemplar, fecha_prestamo, fecha_devolucion,estado)
        prestamo.setNombre(nombre)
        prestamo.setApellido(apellido)
        prestamo.setTitulo(titulo)
        prestamo.setRenovacion(renovacion)
        prestamo.setR_fecha_devolucion(r_fecha_devolucion)
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

def rutPorId(id_prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "select rut from prestamo where id_prestamo = %s"
    valores = (id_prestamo,)
    cursor.execute(consulta,valores,)
   
    for row in cursor:
        rut =  row[0]
        break
    conexion.commit()
    cursor.close()
    conexion.close()
    return rut

def cantidadRenovaciones(id_prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "select COUNT(id_renovacion) as cantidadRenovaciones from renovacion where id_prestamo = %s "
    valores = (id_prestamo,)
    cursor.execute(consulta,valores,)
   
    for row in cursor:
        cantidad_renovaciones =  row[0]
        break
    conexion.commit()
    cursor.close()
    conexion.close()
    return cantidad_renovaciones 

def agregarRenovacion(id_prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "INSERT INTO `renovacion` (`id_renovacion`, `id_prestamo`, `dias_devolucion`) VALUES (NULL, %s, '3')"
    valores = (id_prestamo,)
    cursor.execute(consulta,valores,)
    conexion.commit()
    cursor.close()
    conexion.close()
    return f"Se ha concedido la renovación del libro por 3 días adicionales."

def cantidadLibroRenovado(rut):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT COUNT(DISTINCT e.id_ejemplar) AS cantidad_ejemplares_renovacion FROM renovacion AS r INNER JOIN prestamo AS p ON p.id_prestamo = r.id_prestamo INNER JOIN ejemplar AS e ON e.id_ejemplar = p.id_ejemplar WHERE p.rut = %s;"
    valores = (rut,)
    cursor.execute(consulta,valores,)
    for row in cursor:
        libros_renovados =  row[0]
        break
    conexion.commit()
    cursor.close()
    conexion.close()
    return libros_renovados

   
#SELECT a.rut, a.nombre, a.apellido, t.hora_ingreso, t.hora_salida FROM administrador AS a, time AS t WHERE a.rut = t.rut_admin;

