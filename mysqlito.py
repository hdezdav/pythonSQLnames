import mysql.connector
from mysql.connector import Error

def crear_conexion():
    """Crea conexión a MySQL"""
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',        
            password='fotniteJM',       
            database='usuarios_db'
        )
        return conexion
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

def crear_tabla(conexion):
    """Crea la tabla si no existe"""
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL
            )
        """)
        conexion.commit()
    except Error as e:
        print(f"Error al crear tabla: {e}")

def agregar_usuario(conexion, nombre):
    """Agrega un usuario"""
    if not nombre.strip():
        print("El nombre no puede estar vacío")
        return
    
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre.strip(),))
        conexion.commit()
        print(f"Usuario '{nombre}' agregado correctamente")
    except Error as e:
        print(f"Error: {e}")

def mostrar_usuarios(conexion):
    """Muestra todos los usuarios"""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM usuarios ORDER BY id")
        usuarios = cursor.fetchall()
        
        if not usuarios:
            print("No hay usuarios registrados")
            return False
        
        print("\n--- Lista de usuarios ---")
        for id, nombre in usuarios:
            print(f"{id}. {nombre}")
        print("-" * 25)
        return True
    except Error as e:
        print(f"Error: {e}")
        return False

def editar_usuario(conexion):
    """Edita un usuario"""
    if not mostrar_usuarios(conexion):
        return
    
    try:
        id_usuario = int(input("ID del usuario a editar: "))
        nuevo_nombre = input("Nuevo nombre: ").strip()
        
        if not nuevo_nombre:
            print("El nombre no puede estar vacío")
            return
        
        cursor = conexion.cursor()
        cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nuevo_nombre, id_usuario))
        conexion.commit()
        
        if cursor.rowcount == 0:
            print("ID no encontrado")
        else:
            print("Usuario actualizado correctamente")
            
    except ValueError:
        print("El ID debe ser un número")
    except Error as e:
        print(f"Error: {e}")

def eliminar_usuario(conexion):
    """Elimina un usuario"""
    if not mostrar_usuarios(conexion):
        return
    
    try:
        id_usuario = int(input("ID del usuario a eliminar: "))
        
        # Confirmar eliminación
        confirmar = input(f"¿Eliminar usuario con ID {id_usuario}? (s/n): ").lower()
        if confirmar not in ['s', 'si']:
            print("Operación cancelada")
            return
        
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
        conexion.commit()
        
        if cursor.rowcount == 0:
            print("ID no encontrado")
        else:
            print("Usuario eliminado correctamente")
            
    except ValueError:
        print("El ID debe ser un número")
    except Error as e:
        print(f"Error: {e}")

def main():
    """Función principal"""
    conexion = crear_conexion()
    if not conexion:
        print("No se pudo conectar a la base de datos")
        return
    
    crear_tabla(conexion)
    print("Conectado a MySQL correctamente")
    
    while True:
        print("\n=== Gestión de Usuarios ===")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            nombre = input("Nombre del usuario: ")
            agregar_usuario(conexion, nombre)
            
        elif opcion == "2":
            mostrar_usuarios(conexion)
            
        elif opcion == "3":
            editar_usuario(conexion)
            
        elif opcion == "4":
            eliminar_usuario(conexion)
            
        elif opcion == "5":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción inválida")
    
    conexion.close()

if __name__ == "__main__":
    main()