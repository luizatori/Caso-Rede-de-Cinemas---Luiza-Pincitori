import sqlite3

connection = sqlite3.connect("cinema.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sessao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    horario_inicio TEXT NOT NULL,
    horario_fim TEXT NOT NULL,
    filme_id INTEGER NOT NULL,
    cinema_id INTEGER NOT NULL
)
""")

connection.commit()
connection.close()
