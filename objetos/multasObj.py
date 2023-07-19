class Multa:
    def __init__(self,monto,id_prestamo,fecha_multa,estado):
        self.__monto = monto
        self.__id_prestamo = id_prestamo
        self.__fecha_multa = fecha_multa
        self.__estado = estado
    def setMonto(self,monto):
        self.__monto = monto
    def setId_prestamo(self,id_prestamo):
        self.__id_prestamo = id_prestamo
    def setFecha_multa(self,fecha_multa):
        self.__fecha_multa = fecha_multa
    def setEstado(self,estado):
        self.__estado = estado
    def getMonto(self):
        return self.__monto 
    def getId_prestamo(self):
        return self.__id_prestamo 
    def getFecha_multa(self):
        return self.__fecha_multa 
    def getEstado(self):
        return self.__estado 
    def setEstado(self,estado): 
        self.__estado = estado
