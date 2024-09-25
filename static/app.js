document.getElementById('add-expense').addEventListener('click', addExpense);

async function addExpense() {
    const name = document.getElementById('expense-name').value;
    const amount = parseFloat(document.getElementById('expense-amount').value);
    const date = document.getElementById('expense-date').value;
    const category = document.getElementById('expense-category').value;

    if (name && amount && date && category) {
        const expense = {
            name,
            amount,
            date,
            category
        };

        try {
            // Enviar gasto a la API
            const response = await fetch('/add_expense', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(expense)
            });

            if (response.ok) {
                // Actualizar la lista de gastos
                fetchExpenses();
                // Limpiar los campos del formulario
                document.getElementById('expense-name').value = '';
                document.getElementById('expense-amount').value = '';
                document.getElementById('expense-date').value = '';
                document.getElementById('expense-category').value = '';
            } else {
                const errorData = await response.json();
                alert(`Error: ${errorData.error}`);
            }
        } catch (error) {
            console.error('Error adding expense:', error);
            alert('Error adding expense. Please try again.');
        }
    } else {
        alert('Please fill in all fields.');
    }
}

async function fetchExpenses() {
    try {
        const response = await fetch('/expenses');
        const expenses = await response.json();
        
        const expenseItems = document.getElementById('expense-items');
        expenseItems.innerHTML = '';

        let total = 0;

        expenses.forEach(expense => {
            total += expense.amount;

            const li = document.createElement('li');
            
            const nameSpan = document.createElement('span');
            nameSpan.classList.add('expense-name');
            nameSpan.textContent = expense.name;

            const amountSpan = document.createElement('span');
            amountSpan.classList.add('expense-amount');
            amountSpan.textContent = `$${expense.amount.toFixed(2)}`;

            const dateSpan = document.createElement('span');
            dateSpan.classList.add('expense-date');
            dateSpan.textContent = expense.date;

            li.appendChild(nameSpan);
            li.appendChild(amountSpan);
            li.appendChild(dateSpan);
            expenseItems.appendChild(li);
        });

        document.getElementById('total-expenses').textContent = `$${total.toFixed(2)}`;
    } catch (error) {
        console.error('Error fetching expenses:', error);
    }
}

// Cargar los gastos al cargar la página
window.onload = fetchExpenses;
