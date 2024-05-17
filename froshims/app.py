from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ['Basketball','Soccer','Ultimate Frisbee']

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
    REGISTRANTS[name] = sport

    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)