from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re, os, sys

app = Flask(__name__)

app.secret_key = 'stuff'

app.config['MYSQL_HOST'] = os.environ.get('mysql_host')
app.config['MYSQL_USER'] = os.environ.get('mysql_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('mysql_pass')
app.config['MYSQL_DB'] = 'ansibletest'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s)', (username, password,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)






























# class user(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80))
#     password = db.Column(db.String(80))
#
# @app.route("/")
# def index():
#     return render_template("index.html")



# @app.route("/login",methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         uname = request.form["uname"]
#         passw = request.form["passw"]
#
#         login = user.query.filter_by(username=uname, password=passw).first()
#         if login is not None:
#             return redirect(url_for("index"))
#     return render_template("login.html")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         uname = request.form['uname']
#         passw = request.form['passw']
#
#         register = user(username = uname, password = passw)
#         db.session.add(register)
#         db.session.commit()
#
#         return redirect(url_for("index"))
#     return render_template("register.html")
#
# if __name__ == "__main__":
#     db.create_all()
#     app.run(debug=True)
