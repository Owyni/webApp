from flask import Flask, render_template, redirect, url_for

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

@app.route("/mostrar/<nombre>", methods=["GET", "POST"])
def mostrar_nombre(nombre):
    return render_template("mostrar.html", nombre_parametro = nombre)

@app.errorhandler(404)
def pagina_error(error):
    return render_template("404.html", error=error), 404

@app.route("/redirect")
def mi_redirect():
    return redirect(url_for("hello_world"))