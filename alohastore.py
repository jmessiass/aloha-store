# FLAG: ${AlohaHackingClub-Disclosure}
from flask import Flask, request, render_template, send_from_directory
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/painel-admin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            return render_template('login.html', message="FLAG: ${AlohaHackingClub-SQLi}")
        else:
            return render_template('login.html', message="Credenciais inválidas!")

    return render_template('login.html')

@app.route('/services')
def search():
    query = request.args.get('q', '')
    return render_template('search.html', query=query)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/00search')
def services():
    filename = request.args.get('filename', 'default.txt')
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return render_template('services.html', content=content)
    except FileNotFoundError:
        return render_template('services.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(os.path.join(app.root_path), 'robots.txt')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)