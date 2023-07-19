from objetos.libroObj import *
from DB.ConsultaLibro import *
from tabulate import tabulate
from objetos.UsuarioObj import *
from DB.ConsultaUsuario import *
from DB.conexion import close_connection
from DB.ConsultaPrestamo import *
from objetos.prestamoObj import *
from datetime import datetime , timedelta, date
import hashlib
from objetos.multasObj import *
from DB.cosultaMultas import *
# ///////////////////////////////// funciones extras ////////////////////////////////////////////////
def hasheado(data):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode('utf-8'))
    hashed_data = hash_object.hexdigest()
    return hashed_data


def date_Today():
    return datetime.today().strftime("%Y-%m-%d %H:%M:%S")

def input_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes ingresar una opcion válida.")

# ///////////////////////////////// funciones admin ////////////////////////////////////////////////
rutAdmin = None
fechaInicial = None
def registrar():
    print("Ingrese sus datos para registrarse")
    rut = input_int("Ingrese su Rut: \n")
    if verificarRut(rut) == True:
        print("Este usuario ya esta registrado")
        menu_admin()
    nombre = input("ingrese su Nombre: \n")
    apellido = input("ingrese su Apellido: \n")
    contrasena = input("ingrese su Contraseña: \n")
    contrasenaHash = hasheado(contrasena)
    administrador = Administrador(nombre,apellido,rut,contrasenaHash)
    ingresarAdmin(administrador)
    log_in()
    
def log_in():
        global rutAdmin, fechaInicial
        print("Ingrese sus datos para loguearse")
        rut = input_int("Ingrese su Rut: \n")
        contrasena = input("Ingrese su Contraseña: \n")
        contrasenaHash = hasheado(contrasena)
        administrador = Administrador(None,None,rut,contrasenaHash)
        if verificarAdmin(administrador) == True:
            fecha_in = date_Today()
            fechaInicial = fecha_in
            rutAdmin = rut
            print("Sesion iniciada")

            subMenu_admin()
            return rut
        else:
            print("Contraseña o rut incorrectos")
            menu_admin()
        
def log_out():
    global rutAdmin, fechaInicial
    fecha_out = date_Today()

    time = Time(rutAdmin,fechaInicial, fecha_out)
    registro(time)

# ///////////////////////////////// funciones usuarios ////////////////////////////////////////////////
def ingresarUsuario():
    nombre = input("Ingrese el nombre del Usuario: ")
    apellido = input("Ingrese el apellido del Usuario: ")
    rut = input_int("Ingrese el rut del Usuario sin puntos ni guion: ")
    opcion = input_int("Selecciona el tipo de usuario: \n1.- Docente  \n2.- Estudiante\n")
    if opcion == 1:
        tipo_usuario = 'docente'
    elif opcion == 2:
        tipo_usuario = 'estudiante'
    else:
        print("Opcion inválida. Por favor, selecciona una opcion válida.")
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

    headers = ['Nombre', 'Apellido', 'Rut', 'Tipo usuario', 'Correo', 'Numero telefono']

    tabla = tabulate(datos, headers, tablefmt="grid")
    print(tabla)
    menu_Usuarios()

def buscarUnUsuario(hacer_prestamo = False):
    opcion = 0
    print("¿Como desea buscar el Usuario?\n 1. Por Rut \n 2. Por Nombre")
    while opcion < 1 or opcion > 2:
        opcion = input_int("Selecciona una opcion: ")
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
    print("¿Como desea buscar el libro?: \n1. Por Id \n2. Por Título")
    
    opcion = 0
    while opcion < 1 or opcion > 2:
        opcion = input_int("Selecciona una opcion: ")
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

        headers = ["Id libro", "Autor", "Título", "Género", "Total ejemplares", "Ejemplares disponibles", "Ejemplares en préstamo", "Ejemplares dañados"]

        print(tabulate(table, headers=headers, tablefmt="grid"))

    else:
        buscarOtra = input_int("No se encontro ningún libro.\n¿Desea buscar otro libro? : \n1.- si \n2.- no\n")
        if buscarOtra == 1:
            return buscarUnLibro(hacer_prestamo)
        else:
            menu_libros()
    if hacer_prestamo != True:
        agergarejemplar = input_int("¿Desea agregar un ejemplar? : \n1.- si \n2.- no\n")

        while agergarejemplar == 1:
            id_libro = input_int("indique el id del libro para ingresar")
            agregarUnEjemplar(id_libro)
            print('Ejemplar agregado')
            agergarejemplar = input_int("¿Desea agregar otro ejemplar? : \n1.- si \n2.- no\n")
        menu_libros()
    else:
        if opcion == 1:
            id_libro = libro.getId_libro()
        elif opcion == 2:
            id_libro = input_int('Ingrese el id del libro: ')
        return id_libro    

def agregarUnEjemplar(id_libro):
    id_ejemplar = ' '
    estado = ' '
    ejemplar = Ejemplar(id_ejemplar,id_libro, estado)
    agregar_Un_Ejemplar(ejemplar)

#//////////////////////////////// prestamo funciones///////////////////////////////////////
def DefUsuario(hacer_prestamo):
    rut = buscarUnUsuario(hacer_prestamo)
    tipo = tipoUsuario(rut)
    return rut ,tipo


def DefLibro(hacer_prestamo):
    id_ejemplar = None
    while id_ejemplar == None:
        id_libro = buscarUnLibro(hacer_prestamo)
        id_ejemplar = seleccionarEjemplar(id_libro)
    return id_ejemplar

def crearPrestamo():
    hacer_prestamo = True
    salir = False
    while salir == False :
        rut, tipo = DefUsuario(hacer_prestamo)
        cantidad_Prestamo = cantidadPrestamo(rut)
        multa, monto = consultaMultaRut(rut)
        if multa == True:
            print('El estudiante tiene una multa por pagar:' + str(monto))
            while True:
                opcion = input_int('¿Desea buscar a otro usuario?\n1.- Sí\n2.- No\n')
                if opcion == 2:
                    menu_prestamo()
                    salir = True
                    break
                elif opcion == 1:
                    print('Buscando a otro usuario')
                    break
                else:
                    print('Ingrese una opcion válida')
                
        else:
            if tipo == "docente": 
                diasDevolucion = 20 
                salir = True
            elif tipo == "estudiante":
                diasDevolucion = 7
                if cantidad_Prestamo >= 2: 
                    print('El estudiante ya a sobrepasado la cantidad de prestamos disponibles: '+ str(cantidad_Prestamo))
                    while True:
                        opcion = input_int('¿Desea buscar a otro usuario?\n1.- Sí\n2.- No\n')
                        if opcion == 2:
                            menu_prestamo()
                            salir = True
                            break
                        elif opcion == 1:
                            print('Buscando a otro usuario')
                            break
                        else:
                            print('Ingrese una opcion válida')
                
    
    id_ejemplar = DefLibro(hacer_prestamo)
    id_prestamo = None
    estado = None
    fecha_prestamo = datetime.now().date()
    fecha_devolucion = fecha_prestamo + timedelta(days=diasDevolucion)
    aceptar = input_int('¿Desea realizar el prestamo?: \n1.- Si \n2.- no \n')
    if aceptar == 1:
        prestamo = Prestamo(id_prestamo, rut, id_ejemplar, fecha_prestamo, fecha_devolucion, estado)
        hacerPrestamo(prestamo)
        ejemplarPrestamo(id_ejemplar)
        print('Prestamo ingresado Correctamente')
    else:
        print('Prestamo no realizado')
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
            prestamo.getEstado(),
            prestamo.getRenovacion(),
            prestamo.getR_fecha_devolucion()
        ])

    headers = ['Nombre', 'Apellido', 'Titulo', 'Fecha prestamo', 'Fecha devolucion','Estado','cantidad de renovaciones', 'Nueva fecha de devolucion']

    print(tabulate(datos, headers, tablefmt="grid"))
    menu_prestamo()


def buscarPrestamo():
    where = input_int("Ingrese el rut del usuario: \n")
    prestamos = Buscar_Prestamo(where)

    datos = []
    for prestamo in prestamos:
        datos.append([
            prestamo.getId_prestamo(),
            prestamo.getRut(),
            prestamo.getId_ejemplar(),
            prestamo.getNombre(),
            prestamo.getApellido(),
            prestamo.getTitulo(),
            prestamo.getFecha_prestamo(),
            prestamo.getFecha_devolucion(),
            prestamo.getEstado(),
            prestamo.getRenovacion(),
            prestamo.getR_fecha_devolucion()
        ])
            
    headers = ['Nombre', 'Apellido', 'Titulo', 'Fecha prestamo', 'Fecha devolucion','Estado','cantidad de renovaciones', 'Nueva fecha de devolucion']

    print(tabulate(datos, headers, tablefmt="grid"))
    while True:
        opcion = input_int("¿Desea modificar algun prestamo?:\n1.- si \n2.- no \n")
        if opcion == 1:
            id_prestamo = input_int('Ingrese el Id del prestamo')
            ModificarPrestamo(id_prestamo)
            break
        elif opcion == 2:
            menu_prestamo()
            break
        else: 
            print("Elija una opcion correcta")


def ModificarPrestamo(id_prestamo):
    while True:
        opcion = input_int("¿Que desea hacer con el prestamo?:\n1.- Terminarlo \n2.- Cambiar algo (libro/usuario)\n3._ Hacer una renovacion \n")
        if opcion == 1:
            TerminarPrestamo(id_prestamo)
            cambiarDisponible(id_prestamo)
            menu_prestamo()
            break
        elif opcion == 2:
            cambiarPrestamo(id_prestamo)
            break
        elif opcion == 3:
            renovarLibro(id_prestamo)
            break
        else: 
            print("Elija una opcion correcta")


def cambiarPrestamo(id_prestamo):
    opcion = input_int('¿Que desea cambiar? \n1.- Usuario \n2.-libro')
    if opcion == 1:
        hacer_prestamo = True
        diasDevolucion, rut = DefUsuario(hacer_prestamo)
        valor = rut
        cambio = 'rut'
    elif opcion == 2:
        hacer_prestamo = True
        id_ejemplar = DefLibro(hacer_prestamo)
        ejemplarPrestamo(id_ejemplar)
        cambiarDisponible(id_prestamo)
        valor = id_ejemplar
        cambio = 'id_ejemplar'
    UpPrestamo(id_prestamo,valor,cambio)
    menu_prestamo()


def renovarLibro(id_prestamo):
    rut = rutPorId(id_prestamo)
    tipo_usuario = tipoUsuario(rut)
    cantidad_renovaciones = cantidadRenovaciones(id_prestamo)
    libros_renovados = cantidadLibroRenovado(rut)
    if tipo_usuario == "estudiante":
        if cantidad_renovaciones < 3 and libros_renovados <= 1:
            print(agregarRenovacion(id_prestamo))
        else:
            print("No es posible realizar más renovaciones para este libro o tiene otro libro con una renovacion.")
            menu_prestamo()
    elif tipo_usuario == "docente":
        if cantidad_renovaciones < 3:
            print(agregarRenovacion(id_prestamo))
        else:
            print("No es posible realizar más renovaciones para este libro.")
            menu_prestamo()

# ///////////////////////////////// multas ////////////////////////////////////////////////

def definirMulta():
     monto = 1000
     fechas = ConsultaPrestamos()
     for row in fechas:
        estado = row[0]
        fecha_multa = row [1]
        fecha_devolucion = row[2]
        dias_devolucion = row [3]
        id_prestamo = row[4]
        if estado == "no terminado":
            if fecha_multa is not None:
                fecha_devolucion = fecha_multa
            elif dias_devolucion is not None:
                fecha_devolucion = fecha_devolucion + timedelta(days=int(dias_devolucion))
            diasatraso = int((date.today() - fecha_devolucion).days)
            if diasatraso >= 3: 
                print(fecha_devolucion)
                montoPorAtraso = diasatraso * monto
                fecha_multa = date_Today()
                multa = Multa(montoPorAtraso,id_prestamo,fecha_multa,None)
                ingresarMulta(multa)

def pagarMulta():
    salir = False
    while salir == False:
        rut = input_int('Ingrese el rut del usuario')
        datos, montoTotal = buscarMulta(rut)
        if not datos:
            while True:
                opcion = input_int('Usuario no encontrado \n ¿Desea buscar otro? \n1.-si\n2.-no')
                if opcion == 1:
                    break
                elif opcion == 2:
                    menu()
                    salir = True
                    break
                else:
                    print('Elija una opcion valida')
        else:
            salir = True
    else:
        headers = ['Id prestamo','Nombre','Apellido','Rut','Titulo','Monto','Estado de la multa','Fecha multa']

        print(tabulate(datos, headers=headers, tablefmt="grid"))
        monto = [[montoTotal]]
        print(tabulate(monto , headers=['Monto Total'], tablefmt="grid"))
    
    while True:
        opcion = input_int('¿Desea pagar la multa? \n1.- si \n2.- no\n')
        if opcion == 1:
            id_prestamo = input('Ingrese el Id del prestamo:\n')
            pagar_multa(id_prestamo)
            TerminarPrestamo(id_prestamo)
            menu()
            break
        elif opcion == 2:
            menu()
            break
        else:
            print('Elija una opcion valida')

# ///////////////////////////////// menus ////////////////////////////////////////////////
def menu_Usuarios():
    while True:
        print("===== Menu Usuarios =====\n1. Ingresar Usuario\n2. Mostrar Todos los Usuarios\n3. Buscar Usuario\n4. Salir")
        opcion = input_int("Selecciona una opcion: ")
        
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
            print("Opcion inválida. Por favor, selecciona una opcion válida.")

def menu_libros():
    while True:
        print("===== Menu Libros =====\n1. Ingresar libro\n2. Mostrar libros\n3. Buscar libro\n4. Salir")

        opcion = input_int("Selecciona una opcion: ")

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
            print("Opcion inválida. Por favor, selecciona una opcion válida.")

def menu_prestamo():
    while True:
        print("===== Menu Prestamos =====\n1. hacer un prestamo\n2. Mostrar los prestamos\n3. Buscar un prestamo\n4. Salir")
        opcion = input_int("Selecciona una opcion: ")
        if opcion == 1:
            crearPrestamo()
            break
        elif opcion == 2:
            mostrarPrestamos()
            break
        elif opcion == 3:
            buscarPrestamo()
            break
        elif opcion == 4:
            menu()
            break
        else:
            print("Opcion inválida. Por favor, selecciona una opcion válida.")

def menu():
    while True:
        print("===== Menu Biblioteca =====\n1. Administrar libros\n2. Administrar usuarios\n3. Administrar prestamos\n4. pagar multas\n5. Salir")


        opcion = input_int("Selecciona una opcion: ")

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
            pagarMulta()
            break
        elif opcion == 5:
            subMenu_admin()
            break
        else:
            print("Opcion inválida. Por favor, selecciona una opcion válida.")

def menu_admin():
    while True:
        print("===== Menu Biblioteca =====\1. Registrarse\2. Logearse\3. Salir")

        opcion = input_int("Selecciona una opcion: ")

        if opcion == 1:
            registrar()
            break
        elif opcion == 2:
            log_in()
            break
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opcion inválida. Por favor, selecciona una opcion válida.")


def subMenu_admin():
    while True:
        print("===== Menu Biblioteca =====\n1. Menu\n2. Cerrar sesion")
        print("")
        print("")
        opcion = input_int("Selecciona una opcion: ")

        if opcion == 1:
            menu()
            break
        if opcion == 2:
            log_out()
            menu_admin()
            break
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opcion inválida. Por favor, selecciona una opcion válida.")

definirMulta()
pagarMulta()
