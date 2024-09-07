from flask import Flask, jsonify
from db import create_tables, get_transactions, get_budget

app = Flask(__name__)

@app.route('/api/transactions', methods=['GET'])
def api_get_transactions():
    transactions = get_transactions()
    return jsonify([{'description': t[1], 'amount': t[2]} for t in transactions])

@app.route('/api/budget', methods=['GET'])
def api_get_budget():
    budget = get_budget()
    if budget:
        return jsonify({'total': budget[1], 'spent': budget[2]})
    else:
        return jsonify({'total': None, 'spent': None})

if __name__ == '__main__':
    create_tables()  # Ensure tables are created
    app.run(debug=True)
