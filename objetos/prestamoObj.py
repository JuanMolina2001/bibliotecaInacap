class Prestamo:
    def __init__(self,id_prestamo, rut, id_ejemplar, fecha_prestamo, fecha_devolucion):
        self.__id_prestamo = id_prestamo
        self.__rut = rut
        self.__id_ejemplar = id_ejemplar
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
    def getId_prestamo(self):
        return self.__id_prestamo
    def setId_prestamo(self,id_prestamo):
        self.__id_prestamo = id_prestamo
    def getRut(self):
        return self.__rut
    def setRut(self,rut):
        self.__rut = rut
    def setId_ejemplar(self,id_ejemplar):
        self.__id_ejemplar = id_ejemplar
    def getId_ejemplar(self):
        return self.__rut
    def setId_ejemplar(self,id_ejemplar):
        self.__id_ejemplar = id_ejemplar
    def getId_ejemplar(self):
        return self.__id_ejemplar
    def setFecha_prestamo(self, fecha_prestamo):
        self.__fecha_prestamo = fecha_prestamo
    def getFecha_prestamo(self):
        return self.__fecha_prestamo
    def setFecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion
    def getFecha_devolucion(self):
        return self.__fecha_devolucion
    
