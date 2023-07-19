import subprocess
import tkinter as tk
from tkinter import messagebox
import threading
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def crear_db():
    crear_db_cmd = r'C:\xampp\mysql\bin\mysql.exe -u root -e "CREATE DATABASE biblioteca"'
    sql_content = '''
    SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
    START TRANSACTION;
    SET time_zone = "+00:00";

    CREATE TABLE `administrador` (
    `rut` int(10) NOT NULL,
    `nombre` varchar(50) NOT NULL,
    `apellido` varchar(50) NOT NULL,
    `contrasena` varchar(64) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `administrador` (`rut`, `nombre`, `apellido`, `contrasena`) VALUES
    (208381571, 'hola', 'juan', 'b221d9dbb083a7f33428d7c2a3c3198ae925614d70210e28716ccaa7cd4ddb79');

    CREATE TABLE `ejemplar` (
    `id_ejemplar` int(11) NOT NULL,
    `id_libro` int(11) DEFAULT NULL,
    `estado` enum('Disponible','En prestamo','Danado') NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `ejemplar` (`id_ejemplar`, `id_libro`, `estado`) VALUES
    (1, 101, 'En prestamo'),
    (2, 102, 'En prestamo'),
    (3, 103, 'En prestamo'),
    (4, 101, 'Disponible'),
    (5, 104, 'Disponible');

    CREATE TABLE `libro` (
    `id_libro` int(11) NOT NULL,
    `autor` varchar(100) NOT NULL,
    `titulo` varchar(100) NOT NULL,
    `genero` varchar(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `libro` (`id_libro`, `autor`, `titulo`, `genero`) VALUES
    (101, 'Gabriel Garcia Marquez', 'Cien anos de soledad', 'Realismo'),
    (102, 'J.K. Rowling', 'Harry Potter y la Piedra Filosofal', 'Fantasia'),
    (103, 'George Orwell', '1984', 'Distopia'),
    (104, 'Jane Austen', 'Orgullo y prejuicio', 'Romance');

    CREATE TABLE `multa` (
    `id_multa` int(11) NOT NULL,
    `monto` int(20) NOT NULL,
    `id_prestamo` int(11) DEFAULT NULL,
    `fecha_multa` date NOT NULL,
    `estado` enum('pagado','no pagado') NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `multa` (`id_multa`, `monto`, `id_prestamo`, `fecha_multa`, `estado`) VALUES
    (30, 9000, 101, '2023-07-19', 'pagado'),
    (31, 9000, 102, '2023-07-19', 'no pagado'),
    (32, 7000, 103, '2023-07-19', 'pagado');

    CREATE TABLE `prestamo` (
    `id_prestamo` int(11) NOT NULL,
    `rut` int(11) DEFAULT NULL,
    `id_ejemplar` int(11) DEFAULT NULL,
    `fecha_prestamo` date NOT NULL DEFAULT current_timestamp(),
    `fecha_devolucion` date NOT NULL,
    `estado` enum('no terminado','terminado') NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `prestamo` (`id_prestamo`, `rut`, `id_ejemplar`, `fecha_prestamo`, `fecha_devolucion`, `estado`) VALUES
    (101, 111222333, 1, '2023-06-01', '2023-07-07', 'no terminado'),
    (102, 987654321, 2, '2023-07-03', '2023-07-10', 'no terminado'),
    (103, 111222333, 3, '2023-07-05', '2023-07-12', 'no terminado'),
    (104, 123456789, 4, '2023-07-17', '2023-08-06', 'terminado');

    CREATE TABLE `renovacion` (
    `id_renovacion` int(11) NOT NULL,
    `id_prestamo` int(11) DEFAULT NULL,
    `dias_devolucion` int(10) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `renovacion` (`id_renovacion`, `id_prestamo`, `dias_devolucion`) VALUES
    (2, 101, 3);

    CREATE TABLE `time` (
    `time_id` int(11) NOT NULL,
    `hora_ingreso` datetime DEFAULT NULL,
    `hora_salida` datetime DEFAULT NULL,
    `rut_admin` int(10) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `time` (`time_id`, `hora_ingreso`, `hora_salida`, `rut_admin`) VALUES
    (5, '2023-07-18 16:43:53', '2023-07-18 16:44:02', 208381571);

    CREATE TABLE `usuario` (
    `nombre` varchar(50) NOT NULL,
    `apellido` varchar(50) NOT NULL,
    `rut` int(10) NOT NULL,
    `tipo_usuario` enum('docente','estudiante') NOT NULL,
    `correo` varchar(255) NOT NULL,
    `numero_telefono` int(9) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

    INSERT INTO `usuario` (`nombre`, `apellido`, `rut`, `tipo_usuario`, `correo`, `numero_telefono`) VALUES
    ('Laura', 'Gonzalez', 111222333, 'docente', 'laura.gonzalez@example.com', 934567890),
    ('Maria', 'Perez', 123456789, 'docente', 'maria.perez@example.com', 912345678),
    ('Juan', 'Ramirez', 987654321, 'estudiante', 'juan.ramirez@example.com', 976543210);
    ALTER TABLE `administrador`
    ADD PRIMARY KEY (`rut`);

    ALTER TABLE `ejemplar`
    ADD PRIMARY KEY (`id_ejemplar`),
    ADD KEY `id_libro` (`id_libro`);

    ALTER TABLE `libro`
    ADD PRIMARY KEY (`id_libro`);

    ALTER TABLE `multa`
    ADD PRIMARY KEY (`id_multa`),
    ADD KEY `id_prestamo` (`id_prestamo`);

    ALTER TABLE `prestamo`
    ADD PRIMARY KEY (`id_prestamo`),
    ADD KEY `rut` (`rut`),
    ADD KEY `id_libro` (`id_ejemplar`);

    ALTER TABLE `renovacion`
    ADD PRIMARY KEY (`id_renovacion`),
    ADD KEY `id_prestamo` (`id_prestamo`);

    ALTER TABLE `time`
    ADD PRIMARY KEY (`time_id`),
    ADD KEY `rut_admin` (`rut_admin`);

    ALTER TABLE `usuario`
    ADD PRIMARY KEY (`rut`);

    ALTER TABLE `ejemplar`
    MODIFY `id_ejemplar` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

    ALTER TABLE `libro`
    MODIFY `id_libro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

    ALTER TABLE `multa`
    MODIFY `id_multa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

    ALTER TABLE `prestamo`
    MODIFY `id_prestamo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

    ALTER TABLE `renovacion`
    MODIFY `id_renovacion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

    ALTER TABLE `time`
    MODIFY `time_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

    ALTER TABLE `ejemplar`
    ADD CONSTRAINT `ejemplar_ibfk_1` FOREIGN KEY (`id_libro`) REFERENCES `libro` (`id_libro`);

    ALTER TABLE `multa`
    ADD CONSTRAINT `multa_ibfk_1` FOREIGN KEY (`id_prestamo`) REFERENCES `prestamo` (`id_prestamo`);

    ALTER TABLE `prestamo`
    ADD CONSTRAINT `prestamo_ibfk_1` FOREIGN KEY (`rut`) REFERENCES `usuario` (`rut`),
    ADD CONSTRAINT `prestamo_ibfk_2` FOREIGN KEY (`id_ejemplar`) REFERENCES `ejemplar` (`id_ejemplar`);

    ALTER TABLE `renovacion`
    ADD CONSTRAINT `renovacion_ibfk_1` FOREIGN KEY (`id_prestamo`) REFERENCES `prestamo` (`id_prestamo`);

    ALTER TABLE `time`
    ADD CONSTRAINT `time_ibfk_1` FOREIGN KEY (`rut_admin`) REFERENCES `administrador` (`rut`);

    COMMIT;
    '''
    try:
        subprocess.run(crear_db_cmd, shell=True, check=True)
        sql_bytes = sql_content.encode('utf-8')
        subprocess.run(r'C:\xampp\mysql\bin\mysql.exe -u root biblioteca', input=sql_bytes, shell=True, check=True)

    except subprocess.CalledProcessError as e:
        messagebox.showinfo('Error al crear la base de datos',f"Error al ejecutar el comando: {e}")
        loading_window.after(200, cerrar_ventana)
    else:
        messagebox.showinfo("Carga completada", "La base de datos se creó correctamente.")
        loading_window.after(200, cerrar_ventana)

def cerrar_ventana():
    loading_window.destroy()

def main():
    global loading_window
    loading_window = tk.Tk()
    loading_window.title("Cargando...")
    loading_label = tk.Label(loading_window, text="Cargando la base de datos, por favor espere...")
    loading_label.pack(padx=20, pady=10)
    loading_window_width = 400
    loading_window_height = 100
    center_window(loading_window, loading_window_width, loading_window_height)

    threading.Thread(target=crear_db).start()

    loading_window.mainloop()

if __name__ == "__main__":
    main()