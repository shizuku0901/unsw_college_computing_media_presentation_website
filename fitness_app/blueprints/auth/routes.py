from flask import Blueprint, render_template, redirect, url_for, request, session
from extensions import db

# Blueprint for authentication routes
auth_bp = Blueprint(
    'auth',
    __name__
)

# Route for the register page
@auth_bp.route('/register', methods=['GET', 'POST'])

# Function to handle user registration
def register():
    # Handle POST request for user registration
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        uid = request.form.get('uid')

        # Store user information in the database
        db.collection('users').document(uid).set({
            'name': name,
            'age': int(age),
            'email': email,
        })

        # Redirect to the login page after successful registration
        return redirect(url_for('auth.login'))

    # Render the registration template for GET requests
    return render_template('auth/register.html')

# Route for the login page
@auth_bp.route('/login', methods=['GET', 'POST'])
# Function to handle user login
def login():
    # Handle POST request for user login
    if request.method == 'POST':
        # Get the user ID from the form and store it in the session
        uid = request.form.get('uid')
        session['uid'] = uid
        # Redirect to the welcome page after successful login
        return redirect(url_for('welcome.index'))
    # Render the login template for GET requests
    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    # Clear the session to log out the user
    session.clear()
    # Redirect to the login page after logging out
    return redirect(url_for('auth.login'))