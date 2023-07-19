from DB.conexion import get_connection
from objetos.multasObj import Multa
from datetime import datetime, timedelta

def ingresarMulta(multa):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "INSERT INTO `multa` (`id_multa`, `monto`, `id_prestamo`, `fecha_multa`, `estado`) VALUES (NULL, %s, %s, %s, 'no pagado')"
    valores = (multa.getMonto(),multa.getId_prestamo(),multa.getFecha_multa())
    cursor.execute(consulta, valores)
    conexion.commit()
    conexion.close()

def ConsultaPrestamos():
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT p.estado, m.fecha_multa , p.fecha_devolucion, r.dias_devolucion, p.id_prestamo FROM prestamo p LEFT JOIN renovacion AS r ON r.id_prestamo = p.id_prestamo LEFT JOIN multa AS m ON m.id_prestamo = p.id_prestamo;"
    cursor.execute(consulta,)   
    fechas = cursor.fetchall() 
    cursor.close()
    conexion.close()
    return fechas

def consultaMultaRut(rut):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT sum(m.monto) FROM multa m JOIN prestamo AS p ON p.id_prestamo = m.id_prestamo WHERE p.rut = %s GROUP BY p.rut"
    valores = (rut,)
    cursor.execute(consulta,valores,)
    for row in cursor:
        monto = row[0]
    if monto is not None:
        multa = True
    cursor.close()
    conexion.close()
    return multa, monto

def buscarMulta(rut):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT  p.id_prestamo, u.nombre, u.apellido, p.rut,l.titulo, m.monto, m.estado, m.fecha_multa FROM  prestamo  p LEFT JOIN multa AS m ON m.id_prestamo = p.id_prestamo JOIN usuario AS u ON p.rut = u.rut JOIN ejemplar AS e ON e.id_ejemplar = p.id_ejemplar JOIN libro AS l ON l.id_libro = e.id_libro WHERE p.rut = %s"
    valores = (rut,)
    cursor.execute(consulta,valores,)
    datos = []
    montoTotal = 0
    for row in cursor:
        id_prestamo= row[0]
        nombre = row[1]
        apellido = row[2]
        rut = row[3]
        titulo = row[4]
        monto = row[5]
        estado = row[6]
        fecha = row[7]
        if monto is None:
            monto = 'no tiene multas'
            estado = 'Null'
        else:
            montoTotal = montoTotal + monto
        datos.append([id_prestamo,nombre, apellido, rut, titulo, monto, estado, fecha])

    cursor.close()
    conexion.close()
    return datos, montoTotal

def pagar_multa(id_prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "UPDATE `multa` SET `estado` = 'pagado' WHERE `multa`.`id_prestamo` = %s;"
    valores = (id_prestamo,)
    cursor.execute(consulta, valores)
    conexion.commit()
    conexion.close()

