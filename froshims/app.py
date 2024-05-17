from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

SPORTS = ['Basketball','Soccer','Ultimate Frisbee']
DATABASE = 'froshims.db'


def get_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn, cursor):
    cursor.close()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name:
        return render_template("index.html",sports=SPORTS, error="Missing name")
    if not sport:
        return render_template("index.html",sports=SPORTS , error="Missing sport")
    if sport not in SPORTS:
        return render_template("index.html",sports=SPORTS , error="Invalid sport")
    
    # Remember regustrant
    conn, cursor = get_db()
    
    cursor.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", (name, sport))
    conn.commit()

    close_db(conn, cursor)

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    conn, cursor = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrants")
    registrants = cursor.fetchall()
    print(registrants)
    close_db(conn, cursor)
    return render_template("registrants.html", registrants=registrants)

@app.route("/deregister", methods=['POST'])
def deregister():
    id = request.form.get('id')
    print(id)
    if id:
        conn, cursor = get_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM registrants WHERE id=?",id)
        conn.commit()
        close_db(conn, cursor)
    return redirect("/registrants")