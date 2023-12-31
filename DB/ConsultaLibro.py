from DB.conexion import get_connection
from objetos.libroObj import Libro

def insertar_libro(libro):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "INSERT INTO `libro` (`autor`, `titulo`, `genero`) VALUES (?, ?, ?);"
    valores = (libro.getAutor(), libro.getTitulo(), libro.getGenero())
    cursor.execute(consulta, valores)
    conexion.commit()



def mostrar_libros():
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT l.id_libro, l.titulo, l.autor, l.genero, COUNT(e.id_ejemplar) AS total_ejemplares, SUM(CASE WHEN e.estado = 1 THEN 1 ELSE 0 END) AS ejemplares_disponibles, SUM(CASE WHEN e.estado = 2 THEN 1 ELSE 0 END) AS ejemplares_en_prestamo, SUM(CASE WHEN e.estado = 3 THEN 1 ELSE 0 END) AS ejemplares_danados FROM libro l LEFT JOIN ejemplar e ON l.id_libro = e.id_libro GROUP BY l.id_libro;"
    cursor.execute(consulta)

    libros = []
    for row in cursor:
        id_libro = row[0]
        titulo = row[1]
        autor = row[2]
        genero = row[3]
        total_ejemplares = row[4]
        ejemplares_disponibles = row[5]
        ejemplares_en_prestamo = row[6]
        ejemplares_danados = row[7]

        libro = Libro(id_libro,autor, titulo, genero)
        libro.setTotalEjemplares(total_ejemplares)
        libro.setEjemplaresDisponibles(ejemplares_disponibles)
        libro.setEjemplaresEnPrestamo(ejemplares_en_prestamo)
        libro.setEjemplaresDanados(ejemplares_danados)

        libros.append(libro)

    conexion.close()

    return libros

def agregar_Un_Ejemplar(ejemplar):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "INSERT INTO `ejemplar` (`id_ejemplar`, `id_libro`, `estado`) VALUES (NULL, ?, 1);"
    valores = (ejemplar.getId_libro(),)
    cursor.execute(consulta, valores)
    conexion.commit()
    conexion.close()

def buscar_Libro(where):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT l.id_libro, l.titulo, l.autor, l.genero, COUNT(e.id_ejemplar) AS total_ejemplares, SUM(CASE WHEN e.estado = 'Disponible' THEN 1 ELSE 0 END) AS ejemplares_disponibles, SUM(CASE WHEN e.estado = 'En préstamo' THEN 1 ELSE 0 END) AS ejemplares_en_prestamo, SUM(CASE WHEN e.estado = 'Dañado' THEN 1 ELSE 0 END) AS ejemplares_dañados FROM libro l LEFT JOIN ejemplar e ON l.id_libro = e.id_libro WHERE ? GROUP BY l.id_libro;"
    valores = (where,)
    cursor.execute(consulta, valores)

    libros = []
    for row in cursor:
        id_libro = row[0]
        titulo = row[1]
        autor = row[2]
        genero = row[3]
        total_ejemplares = row[4]
        ejemplares_disponibles = row[5]
        ejemplares_en_prestamo = row[6]
        ejemplares_danados = row[7]

        libro = Libro(id_libro, autor, titulo, genero,)
        libro.setTotalEjemplares(total_ejemplares)
        libro.setEjemplaresDisponibles(ejemplares_disponibles)
        libro.setEjemplaresEnPrestamo(ejemplares_en_prestamo)
        libro.setEjemplaresDanados(ejemplares_danados)

        libros.append(libro)

    conexion.close()

    return libros


def ejemplarPrestamo(id_ejemplar):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "UPDATE `ejemplar` SET `estado` = 2 WHERE `ejemplar`.`id_ejemplar` = ?;"
    valores = (id_ejemplar,)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

    
def ejemplarDisponible(id_ejemplar):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "UPDATE `ejemplar` SET `estado` = 1 WHERE `ejemplar`.`id_ejemplar` = ?;"
    valores = (id_ejemplar,)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    
def cambiarDisponible(id_prestamo):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "UPDATE ejemplar AS e SET e.estado = 1 WHERE e.id_ejemplar IN ( SELECT p.id_ejemplar FROM prestamo AS p WHERE p.id_prestamo = ?);"
    valores = (id_prestamo,)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()
