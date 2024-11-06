from flask import Flask, request
from flask_cors import CORS, cross_origin
import mysql.connector
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='python_user',
        password='ourPassword',
        database='users'
    )

def validate(username,password):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result: 
            db_password = result[0]
            if password == db_password:
                return (True,"")
            else:
                return (False, "INCORRECT PASSWORD")
    except TypeError as e:
        return (False,f"EXCEPTION: {e}")
    return (False,f"UNKNOWN USER {username}")

# post request, with arguments, username and password
@app.route("/login", methods=['POST'])
@cross_origin()
def login():
        username = request.form['username']
        password = request.form['password']

        if validate(username,password)[0]:
            return f"SUCCESS: LOGGED INTO {username}"
        else:
            return f"ERROR: BAD LOGIN {validate(username,password)[1]}"


@app.route("/register", methods=['POST'])
@cross_origin()
def register():
    print(request.form)
    username = request.form['username']
    password = request.form['password']
    firstname = request.form['firstname']
    lastname = request.form['lastname']

    connection = create_connection()
    cursor = connection.cursor()


    cursor.execute("INSERT INTO users (username, password, firstname, lastname) VALUES (%s, %s, %s, %s)", (username, password, firstname, lastname))
    connection.commit()
    return f"NEW USER: {username}"
