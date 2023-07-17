class Prestamo:
    def __init__(self,id_prestamo, rut, id_ejemplar, fecha_prestamo, fecha_devolucion, estado):
        self.__id_prestamo = id_prestamo
        self.__rut = rut
        self.__estado = estado 
        self.__id_ejemplar = id_ejemplar
        self.__fecha_prestamo = fecha_prestamo
        self.__fecha_devolucion = fecha_devolucion
        self.__nombre = None
        self.__apellido = None
        self.__titulo = None
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
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def setApellido(self, apellido):
        self.__apellido = apellido
    def getApellido(self):
        return self.__apellido
    def setTitulo(self,titulo):
        self.__titulo = titulo
    def getTitulo(self):
        return self.__titulo
    def setEstado(self,estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado