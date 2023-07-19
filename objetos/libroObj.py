class Libro:
    def __init__(self, id_libro,autor,titulo, genero):
        self.__id_libro = id_libro
        self.__autor = autor
        self.__titulo = titulo
        self.__genero = genero
        self.__total_ejemplares = None
        self.__ejemplares_disponibles = None
        self.__ejemplares_en_prestamo = None
        self.__ejemplares_danados = None
    def getId_libro(self):
        return self.__id_libro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getGenero(self):
        return self.__genero
    def getTotalEjemplares(self):
        return self.__total_ejemplares
    def setTotalEjemplares(self, total_ejemplares):
        self.__total_ejemplares = total_ejemplares
    def getEjemplaresDisponibles(self):
        return self.__ejemplares_disponibles
    def setEjemplaresDisponibles(self, ejemplares_disponibles):
        self.__ejemplares_disponibles = ejemplares_disponibles
    def getEjemplaresEnPrestamo(self):
        return self.__ejemplares_en_prestamo
    def setEjemplaresEnPrestamo(self, ejemplares_en_prestamo):
        self.__ejemplares_en_prestamo = ejemplares_en_prestamo
    def getEjemplaresDanados(self):
        return self.__ejemplares_danados
    def setEjemplaresDanados(self, ejemplares_danados):
        self.__ejemplares_danados = ejemplares_danados

class Ejemplar:
    def __init__(self,id_ejemplar,id_libro,estado):
        self.__id_ejemplar = id_ejemplar
        self.__id_libro = id_libro
        self.__estado = estado
    def getId_ejemplar(self):
        return self.__id_ejemplar
    def setId_ejemplar(self,id_ejemplar):
        self.__id_ejemplar = id_ejemplar
    def getId_libro(self):
        return self.__id_libro
    def setId_libro(self,id_libro):
        self.__id_libro = id_libro
    def getestado(self): 
        return self.__estado
    def setestado(self,estado): 
        self.__estado = estado



