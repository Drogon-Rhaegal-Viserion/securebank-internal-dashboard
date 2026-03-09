from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'replace_with_a_random_secret_key'

# simple in-memory user/database example
users = {
    'employee': {
        'password': generate_password_hash('password123'),
        'balance': 2500.0,
        'transactions': []
    }
}

@app.route('/')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        session['username'] = username
        return redirect(url_for('dashboard'))
    flash('Invalid credentials', 'error')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    user = users[session['username']]
    return render_template('dashboard.html', balance=user['balance'], transactions=user['transactions'])

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = float(request.form['amount'])
        recipient = request.form['recipient']
        sender = users[session['username']]
        if amount <= 0 or amount > sender['balance']:
            flash('Invalid transfer amount', 'error')
        elif recipient not in users:
            flash('Recipient not found', 'error')
        else:
            sender['balance'] -= amount
            users[recipient]['balance'] += amount
            sender['transactions'].append(f"Sent ${amount} to {recipient}")
            users[recipient]['transactions'].append(f"Received ${amount} from {session['username']}")
            flash('Transfer complete', 'success')
        return redirect(url_for('dashboard'))
    return render_template('transfer.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
