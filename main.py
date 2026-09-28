import sqlite3

conn = sqlite3.connect("casino.db")
cursor = conn.cursor()

# Crear la tabla (solo hace falta una vez, IF NOT EXISTS evita error si ya existe)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cuentas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        puntos INTEGER NOT NULL DEFAULT 1000
    )
""")