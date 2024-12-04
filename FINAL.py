import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import bcrypt
from datetime import datetime

def get_connection():
    """Función para obtener la conexión con la base de datos."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123abcABC@",
        database="login"
    )

# Función para registrar un nuevo usuario
def register():
    def register_user():
        user = reg_username_entry.get()
        pwd = reg_password_entry.get().encode('utf-8')
        
        if user and pwd:
            hashed = bcrypt.hashpw(pwd, bcrypt.gensalt()).decode('utf-8')  # Convertir a cadena de texto
            
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user, hashed))
            conn.commit()
            
            messagebox.showinfo("Registro", "Usuario registrado exitosamente")
            
            cursor.close()
            conn.close()
            
            register_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Por favor, ingrese su usuario y contraseña")

    register_window = tk.Toplevel(root)
    register_window.title("Registrar Usuario")
    register_window.geometry("400x450")  # Tamaño de la ventana de registro
    register_window.resizable(False, False)  # Bloquear el cambio de tamaño
    
    register_frame = tk.LabelFrame(register_window, text="Registro", bg="white")
    register_frame.pack(expand=True)

    tk.Label(register_frame, text="Nuevo Usuario:").grid(row=0, column=0, pady=10)
    tk.Label(register_frame, text="Nueva Contraseña:").grid(row=1, column=0, pady=10)

    reg_username_entry = tk.Entry(register_frame)
    reg_password_entry = tk.Entry(register_frame, show="*")

    reg_username_entry.grid(row=0, column=1, pady=10)
    reg_password_entry.grid(row=1, column=1, pady=10)

    reg_button = tk.Button(register_frame, text="Registrar", command=register_user, bg="red", fg="black", width=20, height=2, font=("Helvetica", 12))
    reg_button.grid(row=2, columnspan=2, pady=20)

# Función para registrar un cliente
def add_client():
    """Función para agregar un cliente a la base de datos."""
    nombre = cliente_nombre_entry.get()

    if nombre:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (nombre) VALUES (%s)", (nombre,))
            conn.commit()

            messagebox.showinfo("Cliente", "Cliente agregado exitosamente")
            cliente_window.destroy()  # Cierra la ventana una vez se haya agregado el cliente
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar el cliente: {err}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Por favor, ingrese el nombre del cliente")

# Función para agregar un producto
def add_product():
    """Función para agregar un producto a la base de datos."""
    nombre = producto_nombre_entry.get()
    descripcion = producto_descripcion_entry.get()
    precio = producto_precio_entry.get()

    if nombre and descripcion and precio:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)", (nombre, descripcion, precio))
            conn.commit()

            messagebox.showinfo("Producto", "Producto agregado exitosamente")
            producto_window.destroy()  # Cierra la ventana una vez se haya agregado el producto
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar el producto: {err}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Por favor, complete todos los campos del producto")

# Función para agregar un departamento
def add_department():
    """Función para agregar un departamento a la base de datos."""
    nombre = departamento_nombre_entry.get()

    if nombre:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO departamentos (nombre) VALUES (%s)", (nombre,))
            conn.commit()

            messagebox.showinfo("Departamento", "Departamento agregado exitosamente")
            department_window.destroy()  # Cierra la ventana una vez se haya agregado el departamento
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo agregar el departamento: {err}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Por favor, ingrese el nombre del departamento")

# Ventana para agregar cliente
def open_client_window():
    """Ventana para agregar cliente."""
    global cliente_nombre_entry
    cliente_window = tk.Toplevel()
    cliente_window.title("Agregar Cliente")
    cliente_window.geometry("400x200")

    cliente_frame = tk.Frame(cliente_window, bg="white")
    cliente_frame.pack(expand=True)

    tk.Label(cliente_frame, text="Nombre del Cliente:").grid(row=0, column=0, pady=10)

    cliente_nombre_entry = tk.Entry(cliente_frame)
    cliente_nombre_entry.grid(row=0, column=1, pady=10)

    add_button = tk.Button(cliente_frame, text="Agregar Cliente", command=add_client, bg="red", fg="black", width=20, height=2, font=("Helvetica", 12))
    add_button.grid(row=1, columnspan=2, pady=20)

# Ventana para agregar producto
def open_product_window():
    """Ventana para agregar producto."""
    global producto_nombre_entry, producto_descripcion_entry, producto_precio_entry
    producto_window = tk.Toplevel()
    producto_window.title("Agregar Producto")
    producto_window.geometry("400x300")

    producto_frame = tk.Frame(producto_window, bg="white")
    producto_frame.pack(expand=True)

    tk.Label(producto_frame, text="Nombre del Producto:").grid(row=0, column=0, pady=10)
    tk.Label(producto_frame, text="Descripción:").grid(row=1, column=0, pady=10)
    tk.Label(producto_frame, text="Precio:").grid(row=2, column=0, pady=10)

    producto_nombre_entry = tk.Entry(producto_frame)
    producto_descripcion_entry = tk.Entry(producto_frame)
    producto_precio_entry = tk.Entry(producto_frame)

    producto_nombre_entry.grid(row=0, column=1, pady=10)
    producto_descripcion_entry.grid(row=1, column=1, pady=10)
    producto_precio_entry.grid(row=2, column=1, pady=10)

    add_button = tk.Button(producto_frame, text="Agregar Producto", command=add_product, bg="red", fg="black", width=20, height=2, font=("Helvetica", 12))
    add_button.grid(row=3, columnspan=2, pady=20)

# Ventana para agregar departamento
def open_department_window():
    """Ventana para agregar departamento."""
    global departamento_nombre_entry
    department_window = tk.Toplevel()
    department_window.title("Agregar Departamento")
    department_window.geometry("400x200")

    department_frame = tk.Frame(department_window, bg="white")
    department_frame.pack(expand=True)

    tk.Label(department_frame, text="Nombre del Departamento:").grid(row=0, column=0, pady=10)

    departamento_nombre_entry = tk.Entry(department_frame)
    departamento_nombre_entry.grid(row=0, column=1, pady=10)

    add_button = tk.Button(department_frame, text="Agregar Departamento", command=add_department, bg="red", fg="black", width=20, height=2, font=("Helvetica", 12))
    add_button.grid(row=1, columnspan=2, pady=20)

# Función para registrar una venta
def add_sale():
    """Función para registrar una venta en la base de datos."""
    fecha = fecha_entry.get()
    cliente_id = cliente_combobox.get().split('(')[-1].strip(')')
    producto_id = producto_combobox.get().split('(')[-1].strip(')')
    departamento_id = departamento_combobox.get().split('(')[-1].strip(')')
    cantidad = cantidad_entry.get()
    precio_unitario = precio_unitario_entry.get()

    if fecha and cliente_id and producto_id and departamento_id and cantidad and precio_unitario:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO ventas (fecha, cliente_id, producto_id, departamento_id, cantidad, precio_unitario)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (fecha, cliente_id, producto_id, departamento_id, cantidad, precio_unitario))
            conn.commit()

            messagebox.showinfo("Ventas", "Venta registrada exitosamente")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se pudo registrar la venta: {err}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Por favor, complete todos los campos")

# Verificar existencia del cliente, producto y departamento antes de continuar con la venta
def verify_and_add_sale():
    """Verifica si el cliente, producto y departamento existen en la base de datos antes de registrar la venta."""
    cliente_id = cliente_combobox.get().split('(')[-1].strip(')')
    producto_id = producto_combobox.get().split('(')[-1].strip(')')
    departamento_id = departamento_combobox.get().split('(')[-1].strip(')')

    # Verificar si el cliente existe
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM clientes WHERE id = %s", (cliente_id,))
    cliente = cursor.fetchone()

    if not cliente:
        messagebox.showinfo("Cliente no encontrado", "El cliente no existe. Por favor, ingrésalo.")
        open_client_window()
        return

    # Verificar si el producto existe
    cursor.execute("SELECT id FROM productos WHERE id = %s", (producto_id,))
    producto = cursor.fetchone()

    if not producto:
        messagebox.showinfo("Producto no encontrado", "El producto no existe. Por favor, ingrésalo.")
        open_product_window()
        return

    # Verificar si el departamento existe
    cursor.execute("SELECT id FROM departamentos WHERE id = %s", (departamento_id,))
    departamento = cursor.fetchone()

    if not departamento:
        messagebox.showinfo("Departamento no encontrado", "El departamento no existe. Por favor, ingrésalo.")
        open_department_window()
        return

    # Si todo es válido, agregar la venta
    add_sale()

# Cargar los comboboxes con datos de la base de datos
def load_combobox_data(combobox, table, id_column, name_column):
    """Carga datos en los comboboxes desde la base de datos."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT {id_column}, {name_column} FROM {table}")
    rows = cursor.fetchall()

    # Añadir los elementos al combobox
    combobox['values'] = [f"{row[1]} ({row[0]})" for row in rows]
    conn.close()

def open_sales_window():
    """Ventana para registrar ventas."""
    global fecha_entry, cliente_combobox, producto_combobox, departamento_combobox, cantidad_entry, precio_unitario_entry
    sales_window = tk.Toplevel()
    sales_window.title("Registrar Venta")
    sales_window.geometry("400x350")
    sales_window.resizable(False, False)

    sales_frame = tk.Frame(sales_window, bg="white")
    sales_frame.pack(expand=True)

    # Etiquetas y campos de entrada
    tk.Label(sales_frame, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, pady=10)
    tk.Label(sales_frame, text="Cliente:").grid(row=1, column=0, pady=10)
    tk.Label(sales_frame, text="Producto:").grid(row=2, column=0, pady=10)
    tk.Label(sales_frame, text="Departamento:").grid(row=3, column=0, pady=10)
    tk.Label(sales_frame, text="Cantidad:").grid(row=4, column=0, pady=10)
    tk.Label(sales_frame, text="Precio Unitario:").grid(row=5, column=0, pady=10)

    fecha_entry = tk.Entry(sales_frame)
    cantidad_entry = tk.Entry(sales_frame)
    precio_unitario_entry = tk.Entry(sales_frame)

    # Comboboxes para seleccionar cliente, producto y departamento
    cliente_combobox = ttk.Combobox(sales_frame)
    producto_combobox = ttk.Combobox(sales_frame)
    departamento_combobox = ttk.Combobox(sales_frame)

    fecha_entry.grid(row=0, column=1, pady=10)
    cliente_combobox.grid(row=1, column=1, pady=10)
    producto_combobox.grid(row=2, column=1, pady=10)
    departamento_combobox.grid(row=3, column=1, pady=10)
    cantidad_entry.grid(row=4, column=1, pady=10)
    precio_unitario_entry.grid(row=5, column=1, pady=10)

    # Cargar las opciones de combobox con datos de la base de datos
    load_combobox_data(cliente_combobox, 'clientes', 'id', 'nombre')
    load_combobox_data(producto_combobox, 'productos', 'id', 'nombre')
    load_combobox_data(departamento_combobox, 'departamentos', 'id', 'nombre')

    # Establecer la fecha del sistema en el campo de fecha
    fecha_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))

    # Botón para registrar la venta
    add_button = tk.Button(sales_frame, text="Añadir Venta", command=verify_and_add_sale, bg="red", fg="black", width=20, height=2, font=("Helvetica", 12))
    add_button.grid(row=6, columnspan=2, pady=20)

    sales_window.mainloop()

# Función de login
def login():
    """Función de login"""
    user = username_entry.get()
    pwd = password_entry.get().encode('utf-8')
    
    if user and pwd:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=%s", (user,))
        result = cursor.fetchone()
        
        if result and bcrypt.checkpw(pwd, result[0].encode('utf-8')):        
            messagebox.showinfo("Login", "Login exitoso")
            open_sales_window()  # Abrir nueva ventana si el login es exitoso
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        
        cursor.close()
        conn.close()
    else:
        messagebox.showwarning("Input Error", "Por favor, ingrese su usuario y contraseña")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Login")
root.geometry("400x450")

root.resizable(False, False)

root.configure(bg="white")

main_frame = tk.Frame(root, bg="white")
main_frame.pack(expand=True)

tk.Label(main_frame, text="Usuario:", bg="white", font=("Helvetica", 14)).grid(row=0, column=0, pady=10)
tk.Label(main_frame, text="Contraseña:", bg="white", font=("Helvetica", 14)).grid(row=1, column=0, pady=10)

username_entry = tk.Entry(main_frame)
password_entry = tk.Entry(main_frame, show="*")

username_entry.grid(row=0, column=1, pady=10)
password_entry.grid(row=1, column=1, pady=10)

login_button = tk.Button(main_frame, text="Login", command=login, bg="red", fg="white", width=15, height=2, font=("Helvetica", 10))
login_button.grid(row=2, columnspan=2, pady=20)

register_button = tk.Button(main_frame, text="Registrar", command=register, bg="red", fg="white", width=15, height=2, font=("Helvetica", 10))
register_button.grid(row=3, columnspan=2, pady=20)

image = tk.PhotoImage(file="C:\\Users\\satel\\Downloads\\Abnercito3.png")
image_label = tk.Label(main_frame, image=image, bg="white")
image_label.image = image
image_label.grid(row=4, columnspan=2, pady=20, padx=20)

root.mainloop()
