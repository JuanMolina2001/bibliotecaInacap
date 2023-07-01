class Persona:
    def __init__(self, nombre, apellido, rut):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rut = rut    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    def getApellido(self):
        return self.__apellido
    def setApellido(self,apellido):
        self.__apellido = apellido
    def getRut(self):
        return self.__rut
    def setRut(self,rut):
        self.__rut = rut


class Administrador(Persona):
    def __init__(self,nombre,apellido,rut,fecha):
        super().__init__(nombre, apellido, rut)
        self.__fecha = fecha
    def getFecha(self):
        return self.__fecha
    def setFecha(self,fecha):
        self.__fecha = fecha


class Usuario(Persona):
    def __init__(self,nombre, apellido, rut,tipo_usuario, correo, numero_telefono):
        super().__init__(nombre, apellido, rut)
        self.__tipo_usuario = tipo_usuario
        self.__correo = correo
        self.__numero_telefono = numero_telefono
    def getTipo_usuario(self):
        return self.__tipo_usuario
    def setTipo_usuario(self,tipo_usuario):
        self.__tipo_usuario = tipo_usuario
    def getCorreo(self):
        return self.__correo
    def setCorreo(self,correo):
        self.__correo = correo
    def getNumero_telefono(self):
        return self.__numero_telefono
    def setNumero_telefono(self,numero_telefono):
        self.__numero_telefono = numero_telefono

 