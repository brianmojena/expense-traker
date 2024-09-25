import sqlite3

# Inicializar la base de datos
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    # Crear la tabla de gastos si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        amount REAL NOT NULL,
                        date TEXT NOT NULL,
                        category TEXT NOT NULL
                    )''')
    
    conn.commit()
    conn.close()

# Insertar un nuevo gasto
def insert_expense(name, amount, date, category):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO expenses (name, amount, date, category)
                      VALUES (?, ?, ?, ?)''', (name, amount, date, category))
    
    conn.commit()
    conn.close()

# Obtener todos los gastos
def get_all_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    
    conn.close()
    return expenses
