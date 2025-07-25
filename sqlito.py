import sqlite3
import os

class GestorNombres:
    def __init__(self, db_name="nombres.db"):
        self.db_name = db_name
        self.crear_tabla()
    
    def crear_tabla(self):
        """Crea la tabla de nombres si no existe"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS nombres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
    
    def agregar_nombre(self, nombre):
        """Agrega un nuevo nombre a la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO nombres (nombre) VALUES (?)", (nombre,))
        conn.commit()
        conn.close()
        print(f"✓ Nombre '{nombre}' agregado exitosamente")
    
    def mostrar_nombres(self):
        """Muestra todos los nombres en la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre FROM nombres ORDER BY id")
        nombres = cursor.fetchall()
        conn.close()
        
        if nombres:
            print("\n--- LISTA DE NOMBRES ---")
            for id_nombre, nombre in nombres:
                print(f"{id_nombre}. {nombre}")
            print("-" * 25)
        else:
            print("No hay nombres registrados")
        
        return nombres
    
    def editar_nombre(self, id_nombre, nuevo_nombre):
        """Edita un nombre existente"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Verificar si el ID existe
        cursor.execute("SELECT nombre FROM nombres WHERE id = ?", (id_nombre,))
        resultado = cursor.fetchone()
        
        if resultado:
            nombre_anterior = resultado[0]
            cursor.execute("UPDATE nombres SET nombre = ? WHERE id = ?", (nuevo_nombre, id_nombre))
            conn.commit()
            print(f"✓ Nombre actualizado: '{nombre_anterior}' → '{nuevo_nombre}'")
        else:
            print(f"❌ No se encontró un nombre con ID {id_nombre}")
        
        conn.close()
    
    def eliminar_nombre(self, id_nombre):
        """Elimina un nombre de la base de datos"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Verificar si el ID existe y obtener el nombre
        cursor.execute("SELECT nombre FROM nombres WHERE id = ?", (id_nombre,))
        resultado = cursor.fetchone()
        
        if resultado:
            nombre = resultado[0]
            cursor.execute("DELETE FROM nombres WHERE id = ?", (id_nombre,))
            conn.commit()
            print(f"✓ Nombre '{nombre}' eliminado exitosamente")
        else:
            print(f"❌ No se encontró un nombre con ID {id_nombre}")
        
        conn.close()

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*40)
    print("    GESTOR DE NOMBRES")
    print("="*40)
    print("1. Agregar nombre")
    print("2. Mostrar todos los nombres")
    print("3. Editar nombre")
    print("4. Eliminar nombre")
    print("5. Salir")
    print("-"*40)

def main():
    gestor = GestorNombres()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Selecciona una opción (1-5): ").strip()
            
            if opcion == "1":
                nombre = input("\nIngresa el nombre: ").strip()
                if nombre:
                    gestor.agregar_nombre(nombre)
                else:
                    print("❌ El nombre no puede estar vacío")
            
            elif opcion == "2":
                gestor.mostrar_nombres()
            
            elif opcion == "3":
                nombres = gestor.mostrar_nombres()
                if nombres:
                    try:
                        id_editar = int(input("\nIngresa el ID del nombre a editar: "))
                        nuevo_nombre = input("Ingresa el nuevo nombre: ").strip()
                        if nuevo_nombre:
                            gestor.editar_nombre(id_editar, nuevo_nombre)
                        else:
                            print("❌ El nuevo nombre no puede estar vacío")
                    except ValueError:
                        print("❌ Por favor ingresa un ID válido (número)")
            
            elif opcion == "4":
                nombres = gestor.mostrar_nombres()
                if nombres:
                    try:
                        id_eliminar = int(input("\nIngresa el ID del nombre a eliminar: "))
                        confirmacion = input(f"¿Estás seguro de eliminar el nombre con ID {id_eliminar}? (s/n): ").lower()
                        if confirmacion in ['s', 'si', 'sí']:
                            gestor.eliminar_nombre(id_eliminar)
                        else:
                            print("Operación cancelada")
                    except ValueError:
                        print("❌ Por favor ingresa un ID válido (número)")
            
            elif opcion == "5":
                print("\n¡Gracias por usar el Gestor de Nombres!")
                break
            
            else:
                print("❌ Opción no válida. Por favor selecciona una opción del 1 al 5")
        
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()