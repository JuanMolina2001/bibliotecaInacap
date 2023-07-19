from DB.conexion import get_connection
from objetos.UsuarioObj import Usuario

def ingresar_Usuario(usuario):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "INSERT INTO `usuario` (`nombre`, `apellido`, `rut`, `tipo_usuario`, `correo`, `numero_telefono`) VALUES (%s, %s, %s, %s, %s, %s);"
    valores = (usuario.getNombre(), usuario.getApellido(), usuario.getRut(), usuario.getTipo_usuario(), usuario.getCorreo(), usuario.getNumero_telefono())
    cursor.execute(consulta, valores)
    conexion.commit()

def mostrar_Usuarios():
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT * FROM `usuario`;"
    cursor.execute(consulta)

    usuarios = []
    for row in cursor:
        nombre = row[0]
        apellido = row[1]
        rut = row[2]
        tipo_usuario = row[3]
        correo = row[4]
        numero_telefono = row[5]
        usuario = Usuario(nombre, apellido, rut, tipo_usuario, correo, numero_telefono)

        usuarios.append(usuario)

    conexion.close()

    return usuarios


def buscar_usuario(where):
    conexion = get_connection()
    cursor = conexion.cursor()

    consulta = "SELECT * FROM `usuario` WHERE " + where + " ;"
    cursor.execute(consulta)


    usuarios = []
    for row in cursor:
        nombre = row[0]
        apellido = row[1]
        rut = row[2]
        tipo_usuario = row[3]
        correo = row[4]
        numero_telefono = row[5]
        usuario = Usuario(nombre, apellido, rut, tipo_usuario, correo, numero_telefono)

        usuarios.append(usuario)

    conexion.close()

    return usuarios

def tipoUsuario(rut):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT tipo_usuario from usuario WHERE rut = %s"
    valores = (rut,)
    cursor.execute(consulta, valores)
    for row in cursor:
        tipo_usuario = row[0]
    cursor.close()
    conexion.close()

    return tipo_usuario

def verificarAdmin(administrador):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT contrasena FROM `administrador` WHERE rut = %s;"
    valores = (administrador.getRut(),)
    cursor.execute(consulta, valores)
    contrasena = None
    for row in cursor:
        contrasena = row[0]
        break
    conexion.close()
    if  contrasena == administrador.getContrasena():
        logeado = True
    else:
        logeado = False
    return logeado

def ingresarAdmin(administrador):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "INSERT INTO `administrador` (`rut`, `nombre`, `apellido`, `contrasena`) VALUES (%s, %s, %s, %s);"
    valores = (administrador.getRut(), administrador.getNombre(), administrador.getApellido(), administrador.getContrasena())
    cursor.execute(consulta, valores)
    conexion.commit()

def registro(time):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "INSERT INTO `time` (`time_id`, `hora_ingreso`, `hora_salida`, `rut_admin`) VALUES (NULL, %s, %s, '%s')"
    valores = (time.getFecha_in(),time.getFecha_out(),time.getRut())
    cursor.execute(consulta, valores)
    conexion.commit()

def verificarRut(rut):
    conexion = get_connection()
    cursor = conexion.cursor()
    consulta = "SELECT rut FROM `administrador` WHERE rut = "+ str(rut) +";"
    cursor.execute(consulta)
    rutConsulta= None
    for row in cursor:
        rutConsulta = row[0]
        break
    conexion.close()
    if  rutConsulta == rut:
        registrado = True
    else:
        registrado = False
    return registrado