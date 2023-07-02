from pickle import FALSE, TRUE
from objetos.libroObj import *
from DB.ConsultaLibro import *
from tabulate import tabulate
from objetos.UsuarioObj import *
from DB.ConsultaUsuario import *
from DB.conexion import close_connection
from DB.ConsultaPrestamo import *
from objetos.prestamoObj import *
from datetime import datetime , timedelta

# ///////////////////////////////// funciones usuarios ////////////////////////////////////////////////
def ingresarUsuario():
    nombre = input("Ingrese el nombre del Usuario: ")
    apellido = input("Ingrese el apellido del Usuario: ")
    rut = input_int("Ingrese el rut del Usuario sin puntos ni guion: ")
    opcion = input_int("Selecciona el tipo de usuario: \n 1.- Docente  \n 2.- Estudiante\n")
    if opcion == 1:
        tipo_usuario = 'docente'
    elif opcion == 2:
        tipo_usuario = 'estudiante'
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
    correo = input("Ingrese el correo del Usuario: ")
    numero_telefono = input_int("Ingrese el numero de telefono del Usuario: ")
    usuario = Usuario(nombre, apellido, rut, tipo_usuario, correo, numero_telefono)
    ingresar_Usuario(usuario)
    print('Usuario ingresado Correctamente')
    menu_Usuarios()

def mostrarUsuarios():
    usuarios = mostrar_Usuarios()

    datos = []
    for usuario in usuarios:
        datos.append([
            usuario.getNombre(),
            usuario.getApellido(),
            usuario.getRut(),
            usuario.getTipo_usuario(),
            usuario.getCorreo(),
            usuario.getNumero_telefono(),
        ])

    headers = ['nombre', 'apellido', 'rut', 'tipo usuario', 'correo', 'numero telefono']

    tabla = tabulate(datos, headers, tablefmt="grid")
    print(tabla)
    menu_Usuarios()

def buscarUnUsuario(hacer_prestamo = False):
    opcion = 0
    print("Cómo desea buscar el Usuario")
    print("1. Por Rut")
    print("2. Por Nombre")
    while opcion < 1 or opcion > 2:
        opcion = input_int("Selecciona una opción: ")
        if opcion == 1:
            rut = input_int("Ingrese el rut del Usuario sin puntos ni guion a buscar: ")
            where = "rut = " + str(rut)
            usuarios = buscar_usuario(where) 
            break
        elif opcion == 2:
            nombre = input("Ingresa el Nombre del Usuario a buscar: ")
            where = "nombre LIKE CONCAT('%', '" + nombre + "', '%')"
            usuarios = buscar_usuario(where)
            break
        else: 
            print("Opcion no valida")
    
    if usuarios:
        table = []
        for usuario in usuarios:
            table.append([
                usuario.getNombre(),
                usuario.getApellido(),
                usuario.getRut(),
                usuario.getTipo_usuario(),
                usuario.getCorreo(),
                usuario.getNumero_telefono(),
            ])

        headers = ['nombre', 'apellido', 'rut', 'tipo usuario', 'correo', 'numero telefono']

        print(tabulate(table, headers=headers, tablefmt="grid"))

    else:
        print('No se enecontro ningun Usurio')
        if hacer_prestamo == False:
            menu_Usuarios()
        else:
            menu_prestamo()
    if hacer_prestamo == True:
        if opcion == 1:
            rut = usuario.getRut()
        else:
            rut = input_int("Ingrese el rut del Usuario sin puntos ni guion: ")
        return rut
    else:
        menu_Usuarios()
# ///////////////////////////////// funciones Libros ////////////////////////////////////////////////

def ingresarLibro():
    id_libro = ''
    autor = input("Ingrese el autor del libro: ")
    titulo = input("Ingrese el título del libro: ")
    genero = input("Ingrese el género del libro: ")
    libro = Libro(id_libro,autor, titulo, genero)
    insertar_libro(libro)
    print('Libro ingresado Correctamente')
    menu_libros()


def mostrarLibros():
    libros = mostrar_libros()

    datos = []
    for libro in libros:
        datos.append([
            libro.getId_libro(),
            libro.getAutor(),
            libro.getTitulo(),
            libro.getGenero(),
            libro.getTotalEjemplares(),
            libro.getEjemplaresDisponibles(),
            libro.getEjemplaresEnPrestamo(),
            libro.getEjemplaresDanados()
        ])

    headers = ["Id_libro", "Autor", "Título", "Género", "Total ejemplares", "Ejemplares disponibles", "Ejemplares en préstamo", "Ejemplares dañados"]

   
    print(tabulate(datos, headers, tablefmt="grid"))
    menu_libros()

    
def buscarUnLibro(hacer_prestamo = False):
    print("Cómo desea buscar el libro")
    print("1. Por Id")
    print("2. Por Título")
    opcion = 0
    while opcion < 1 or opcion > 2:
        opcion = input_int("Selecciona una opción: ")
        if opcion == 1:
            id_libro = input_int("Ingresa el ID del libro a buscar: ")
            where = "l.id_libro = " + str(id_libro)
            libros = buscar_Libro(where) 

        elif opcion == 2:
            titulo_libro = input("Ingresa el Título del libro a buscar: ")
            where = "l.titulo LIKE CONCAT('%', '" + titulo_libro + "', '%')"
            libros = buscar_Libro(where)
        else:
            print('Opcion no valida')
    
    if libros:
        table = []
        for libro in libros:
            table.append([
                libro.getId_libro(),
                libro.getAutor(),
                libro.getTitulo(),
                libro.getGenero(),
                libro.getTotalEjemplares(),
                libro.getEjemplaresDisponibles(),
                libro.getEjemplaresEnPrestamo(),
                libro.getEjemplaresDanados()
            ])

        headers = ["Id_libro", "Autor", "Título", "Género", "Total ejemplares", "Ejemplares disponibles", "Ejemplares en préstamo", "Ejemplares dañados"]

        print(tabulate(table, headers=headers, tablefmt="grid"))

    else:
        buscarOtra = input_int("No se encontró ningún libro.\n ¿Desea buscar otro libro? : \n 1.- si \n 2.- no\n")
        if buscarOtra == 1:
            buscarUnLibro()
        else:
            menu_libros()
    if hacer_prestamo != True:
        agergarejemplar = input_int("¿Desea agregar un ejemplar? : \n 1.- si \n 2.- no\n")

        while agergarejemplar == 1:
            id_libro = input_int("indique el id del libro para ingresar")
            agregarUnEjemplar(id_libro)
            print('Ejemplar agregado')
            agergarejemplar = input_int("¿Desea agregar otro ejemplar? : \n 1.- si \n 2.- no\n")
        menu_libros()
    else:
        if opcion == 1:
            id_libro = libro.getId_libro()
        elif opcion == 2:
            id_libro = input_int('ingrese el id del libro: ')
        return id_libro    

def agregarUnEjemplar(id_libro):
    id_ejemplar = ' '
    estado = ' '
    ejemplar = Ejemplar(id_ejemplar,id_libro, estado)
    agregar_Un_Ejemplar(ejemplar)

#//////////////////////////////// prestamo funciones///////////////////////////////////////
def crearPrestamo():
    hacer_prestamo = True
    while True :
        rut = buscarUnUsuario(hacer_prestamo)
        tipo = tipoUsuario(rut)
        if tipo == "docente": 
            cantidad_Prestamo = cantidadPrestamo(rut)
            if cantidad_Prestamo == 2: #cambiar por cantidad de prestamos disponibles docente
                print('el usuario ya a sobrepasado la cantidad de prestamos disponibles: '+ str(cantidad_Prestamo))
                opcion = input_int('desea buscar a otro usuario: \n 1.- si \n 2.- no \n')
                if opcion == 2: 
                    menu_prestamo()
                    break
            else:
                diasDevolucion = 14 #cambiar por cantidad dias para devolver el libro docente
                break

        elif tipo == "estudiante":
            cantidad_Prestamo = cantidadPrestamo(rut)
            if cantidad_Prestamo == 1: #cambiar por cantidad de prestamos disponibles estudiante
                print('el '+ tipo +' ya a sobrepasado la cantidad de prestamos disponibles: '+ str(cantidad_Prestamo))
                opcion = input_int('desea buscar a otro usuario: \n 1.- si \n 2.- no \n')
                if opcion == 2: 
                    menu_prestamo()
                    break
            else:
                diasDevolucion = 7 #cambiar por cantidad dias para devolver el libro docente
                break
    id_ejemplar = None
    while id_ejemplar == None:
        id_libro = buscarUnLibro(hacer_prestamo)
        id_ejemplar = seleccionarEjemplar(id_libro)
    id_prestamo = None
    fecha_prestamo = datetime.now().date()
    fecha_devolucion = fecha_prestamo + timedelta(days=diasDevolucion)
    aceptar = input_int('¿Desea realizar el prestamo?: \n 1.- Si \n 2.- no \n')
    if aceptar == 1:
        prestamo = Prestamo(id_prestamo, rut, id_ejemplar, fecha_prestamo, fecha_devolucion)
        hacerPrestamo(prestamo)
        ejemplarPrestamo(id_ejemplar)
        print('prestamo ingresado Correctamente')
    else:
        print('prestamo no realizado')
    menu_prestamo()

def mostrarPrestamos():
    prestamos = mostrarTodosPrestamos()

    datos = []
    for prestamo in prestamos:
        datos.append([
            prestamo.getNombre(),
            prestamo.getApellido(),
            prestamo.getTitulo(),
            prestamo.getFecha_prestamo(),
            prestamo.getFecha_devolucion(),
        ])

    headers = ['Nombre', 'Apellido', 'Titulo', 'Fecha_prestamo', 'Fecha_devolucion']

    print(tabulate(datos, headers, tablefmt="grid"))
    menu_prestamo()
def ModificarPrestamo():
    pass
def TerminarPrestamo():
    pass
def buscarUnUsuario():
    pass
# ///////////////////////////////// menus ////////////////////////////////////////////////
def input_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar una opcion válida.")



def menu_Usuarios():
    while True:
        print("===== Menu Usuarios =====")
        print("1. Ingresar Usuario")
        print("2. Mostrar Todos los Usuarios")
        print("3. Buscar Usuario")
        print("4. Salir")

        opcion = input_int("Selecciona una opción: ")
        
        if opcion == 1:
            ingresarUsuario()
            break
        elif opcion == 2:
            mostrarUsuarios()
            break
        elif opcion == 3:
            buscarUnUsuario()
            break
        elif opcion == 4:
            menu()
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def menu_libros():
    while True:
        print("===== Menu Libros =====")
        print("1. Ingresar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Salir")

        opcion = input_int("Selecciona una opción: ")

        if opcion == 1:
            ingresarLibro()
            break
        elif opcion == 2:
            mostrarLibros()
            break
        elif opcion == 3:
            buscarUnLibro()
            break
        elif opcion == 4:
            menu()
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def menu_prestamo():
    while True:
        print("===== Menu Prestamos =====")
        print("1. hacer un prestamo")
        print("2. Modificar prestamo")
        print("3. Terminar prestamo")
        print("4. Mostrar los prestamos")
        print("5. Buscar un prestamo")
        print("6. Salir")
        opcion = input_int("Selecciona una opción: ")

        if opcion == 1:
            crearPrestamo()
            break
        elif opcion == 2:
            ModificarPrestamo()
            break
        elif opcion == 3:
            TerminarPrestamo()
            break
        elif opcion == 4:
            mostrarPrestamos()
            break
        elif opcion == 5:
            buscarPrestamo()
            break
        elif opcion == 6:
            menu_prestamo
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def menu():
    while True:
        print("===== Menu Biblioteca =====")
        print("1. Administrar libros")
        print("2. Administrar usuarios")
        print("3. Administrar prestamos")
        print("4. Salir")

        opcion = input_int("Selecciona una opción: ")

        if opcion == 1:
            menu_libros()
            break
        elif opcion == 2:
            menu_Usuarios()
            break
        elif opcion == 3:
            menu_prestamo()
            break
        elif opcion == 4:
            print("¡Hasta luego!")
            break
            close_connection()
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


menu()