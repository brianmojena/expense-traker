from flask import Flask, request, jsonify, render_template
from db import init_db, insert_expense, get_all_expenses
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS si es necesario

# Inicializar la base de datos al inicio
init_db()

# Ruta para servir la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para añadir un nuevo gasto
@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    name = data.get('name')
    amount = data.get('amount')
    date = data.get('date')
    category = data.get('category')
    
    if not all([name, amount, date, category]):
        return jsonify({"error": "Missing data"}), 400
    
    insert_expense(name, amount, date, category)
    return jsonify({"message": "Expense added successfully"}), 201

# Ruta para obtener todos los gastos
@app.route('/expenses', methods=['GET'])
def expenses():
    expenses = get_all_expenses()
    expenses_list = []
    for expense in expenses:
        expenses_list.append({
            "id": expense[0],
            "name": expense[1],
            "amount": expense[2],
            "date": expense[3],
            "category": expense[4]
        })
    
    return jsonify(expenses_list)

if __name__ == '__main__':
    app.run(debug=True)
