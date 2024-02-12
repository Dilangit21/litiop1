from flask import Flask, url_for, render_template, redirect, request
from werkzeug.security import generate_password_hash
from flask_mysqldb import MySQL

litiop1App = Flask(__name__) 
db = MySQL(litiop1App)

@litiop1App.route('/') 
def index():
    return render_template('home.html')

@litiop1App.route('/signup', methods=['GET','POST'])
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

@litiop1App.route('/signin')
def signin():
    return render_template('user.html')

@litiop1App.route('/signout')
def signout():
    return render_template('home.html')

if __name__ == '__main__':
    litiop1App.run (port=3300,debug=True)