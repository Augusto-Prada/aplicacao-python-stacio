from flask import Flask, request, redirect, url_for, session, render_template, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from db import create_tables, add_user, get_user, add_transaction, get_transactions, set_budget, get_budget

app = Flask(__name__)
app.secret_key = 'your_secret_key'

create_tables()

# Home Route
@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        return 'Invalid credentials'
    return render_template('login.html')

# Logout Route
#@app.route('/logout')
#def logout():
 #   session.pop('username', None)
  #  return redirect(url_for('login'))
    @app.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Limpa a sessão
    return redirect(url_for('login')) 

# Dashboard Route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        if 'add_transaction' in request.form:
            description = request.form['description']
            amount = float(request.form['amount'])
            date = request.form['date']
            add_transaction(description, amount, date)
        elif 'set_budget' in request.form:
            total = float(request.form['total'])
            spent = float(request.form['spent'])
            set_budget(total, spent)
    
    transactions = get_transactions()
    budget = get_budget()
    return render_template('dashboard.html', transactions=transactions, budget=budget)


# API for Transactions
@app.route('/api/transactions', methods=['GET'])
def api_get_transactions():
    transactions = get_transactions()
    return jsonify([{'description': t[1], 'amount': t[2]} for t in transactions])
    print ('description')

# API for Budget
@app.route('/api/budget', methods=['GET'])
def api_get_budget():
    budget = get_budget()
    if budget:
        return jsonify({'total': budget[1], 'spent': budget[2]})
    else:
        return jsonify({'total': None, 'spent': None})

if __name__ == '__main__':
    app.run(debug=True)
