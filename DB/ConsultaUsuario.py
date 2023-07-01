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