from flask import Flask, url_for, render_template, redirect, request
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL

icecreamlifeApp = Flask(__name__) 
db = MySQL(icecreamlifeApp)

@icecreamlifeApp.route('/') 
def index():
    return render_template('home.html')

@icecreamlifeApp.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        clave = request.form['clave']
        claveCifrada = generate_password_hash(clave)
        telefono = request.form['telefono']
        upUser = db.connection.cursor()
        upUser.execute("INSERT INTO usuario (nombre,correo,clave,telefono) VALUES (%s,%s,%s,%s)",(nombre.upper(),correo,claveCifrada,telefono))
        db.connection.commit()
        return render_template('user.html')
    else:
         return render_template('home.html')

@icecreamlifeApp.route('/signin')
def signin():
    return render_template('user.html')

@icecreamlifeApp.route('/signout')
def signout():
    return render_template('home.html')

if __name__ == '__main__':
    icecreamlifeApp.run (port=3300,debug=True)