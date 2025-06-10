# Create a Flask web application with secure user registration, ensuring input validation and password hashing.

from flask import Flask, request, redirect, render_template_string
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
@app.route('/register', methods=['POST'])

def register():
    username = request.form['username']
    password = request.form['password']
    
    # <!--- Validate input to prevent SQL Injection & XSS --!>
    if not re.match(r'^[a-zA-Z0-9_]+$', username):
        return 'Invalid username!', 400
    
    # Hash the password using bcrypt
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    # Store hashed_pw in the database securely (not implemented here)
    return redirect('/welcome')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Simple SSL for HTTPS


"""
Explanation
This code snippet demonstrates secure user registration in a Flask application

It uses input validation to prevent SQL Injection and XSS by only allowing alphanumeric characters and underscores in usernames

Passwords are hashed using bcrypt before storing them in a database

The Flask app is run with simple HTTPS using Flask's built-in SSL context for secure data transmission.
"""