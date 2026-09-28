#=============================
# DATA BASE
#=============================
# Funciones que manejan la base de datos SQLite. Asi no se toca la base de datos directamente desde el codigo
 
import sqlite3
 
DB_NAME = "casino.db"  # nombre del archivo .db, se crea solo en la raíz del proyecto
 
 
def conectar():
    """
    Abre una conexión a la base de datos. Permite acceder por nombre
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
 
 
def crear_tablas():
    """
    Crea la tabla 'cuentas' si no existe todavía.
    """
    with conectar() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cuentas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                puntos INTEGER NOT NULL DEFAULT 1000,
                creado_en TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
 
 
# ---------------------------------------------------------------------------
# LECTURA
# ---------------------------------------------------------------------------
 
def obtener_cuenta(nombre):
    """Devuelve la fila de una cuenta por su nombre, o None si no existe."""
    with conectar() as conn:
        return conn.execute(
            "SELECT * FROM cuentas WHERE nombre = ?", (nombre,)
        ).fetchone()
 
 
def listar_cuentas():
    """Devuelve todas las cuentas, ordenadas de más a menos puntos."""
    with conectar() as conn:
        return conn.execute(
            "SELECT * FROM cuentas ORDER BY puntos DESC"
        ).fetchall()
 
 
# ---------------------------------------------------------------------------
# ESCRITURA
# ---------------------------------------------------------------------------
 
def crear_cuenta(nombre, puntos=1000):
    """Crea una cuenta nueva con puntos iniciales (1000 por defecto)."""
    with conectar() as conn:
        conn.execute(
            "INSERT INTO cuentas (nombre, puntos) VALUES (?, ?)", (nombre, puntos)
        )
 
 
def modificar_puntos(nombre, cantidad):
    """Suma una cantidad de puntos a la cuenta indicada. La cantidad puede ser negativa."""
    
    with conectar() as conn:
        conn.execute(
            "UPDATE cuentas SET puntos = puntos + ? WHERE nombre = ?", (cantidad, nombre)
        )
 
 
def renombrar_cuenta(nombre_actual, nombre_nuevo):
    """Cambia el nombre de una cuenta existente."""
    with conectar() as conn:
        conn.execute(
            "UPDATE cuentas SET nombre = ? WHERE nombre = ?", (nombre_nuevo, nombre_actual)
        )
 
 
def eliminar_cuenta(nombre):
    """Borra una cuenta por completo."""
    with conectar() as conn:
        conn.execute("DELETE FROM cuentas WHERE nombre = ?", (nombre,))