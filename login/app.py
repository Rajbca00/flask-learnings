from flask import Flask, render_template, request, redirect, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    """
    Route decorator for the homepage. Renders the index.html template with the logged-in user's name.
    """
    return render_template('index.html', name=session.get('name'))

@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Route decorator for handling the login functionality. 
    If the request method is POST, retrieves the 'name' from the form and stores it in the session.
    Redirects to the homepage if POST, otherwise renders the 'login.html' template.
    """
    if request.method == 'POST':
        name = request.form.get('name')
        session['name'] = name
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():    
    """
    A route decorator that handles the '/logout' endpoint. 
    Clears the session and redirects the user to the home page.
    """
    session.clear()
    return redirect('/')