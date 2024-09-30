from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

#Hay algún error en la variable nombre que no me deja usar las funciones de un string!
@app.route("/saludo/<nombre>")
def amorcin(nombre):
    return f"<h1>Hola {nombre}, te saluda Owynn, el Dios creador de esta página Web</h1>"

@app.route("/math/<int:edad>")
def numero(edad):
    return f"<h2>Tengo {edad} años"