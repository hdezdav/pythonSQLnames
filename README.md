# 📋 Gestor de Usuarios - Python

Este repositorio contiene dos versiones de una aplicación para gestionar usuarios:

- **`sqlito.py`** - Versión con SQLite (no requiere instalación adicional)
- **`mysqlito.py`** - Versión con MySQL (requiere configuración)

---

## 🗄️ Versión SQLite

La versión SQLite funciona directamente sin configuración adicional, ya que SQLite viene incluido con Python. Solo ejecuta:

```bash
python sqlito.py
```

---

## 🐬 Versión MySQL

### ⚙️ Requisitos Previos

Para usar la versión MySQL necesitas tener MySQL Server instalado y funcionando en tu sistema.

### 📦 Instalación de Dependencias

1. **Instala el conector de MySQL:**
   ```bash
   pip install mysql-connector-python
   ```

### 🗃️ Configuración de Base de Datos

2. **Conecta a MySQL como administrador:**
   ```bash
   mysql -u root -p
   ```

3. **Crea la base de datos:**
   ```sql
   CREATE DATABASE usuarios_db;
   EXIT;
   ```

### 🔧 Configuración de Credenciales

4. **Edita las credenciales en `mysqlito.py`:**
   ```python
   conexion = mysql.connector.connect(
       host='localhost',
       user='root',        # Tu usuario de MySQL
       password='tu_password',  # Tu contraseña de MySQL
       database='usuarios_db'
   )
   ```

### 🚀 Ejecución

5. **Ejecuta la aplicación:**
   ```bash
   python mysqlito.py
   ```

---

## 📱 Funcionalidades

Ambas versiones incluyen:

- ✅ **Agregar usuarios** - Solicita nombre y lo guarda
- ✅ **Ver usuarios** - Lista todos los usuarios registrados
- ✅ **Editar usuarios** - Modifica el nombre de un usuario existente
- ✅ **Eliminar usuarios** - Borra un usuario con confirmación
- ✅ **Interfaz simple** - Menú fácil de usar

