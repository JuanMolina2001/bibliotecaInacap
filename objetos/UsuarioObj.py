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
    def __init__(self,nombre,apellido,rut,contrasena):
        super().__init__(nombre, apellido, rut)
        self.__contrasena = contrasena
    def getContrasena(self):
        return self.__contrasena
    def setContrasena(self,contrasena):
        self.__contrasena = contrasena

class Time():
    def __init__(self,fecha_in,fecha_out):
        self.__fecha_in = fecha_in
        self.__fecha_out = fecha_out
    def getFecha_in(self):
        return self.__fecha_in
    def setFecha_in(self,fecha_in):
        self.__fecha_in = fecha_in
    def getFecha_out(self):
        return self.__fecha_out
    def setFecha_out(self,fecha_out):
        self.__fecha_out = fecha_out

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

 