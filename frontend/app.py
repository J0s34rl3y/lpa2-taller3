"""
Frontend Flask para la API de Música
"""

import requests
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "secret-key-for-session"

# URL de la API backend
API_URL = "http://localhost:8002/api"


@app.route("/")
def index():
    """Página principal"""
    return render_template("index.html")


@app.route("/usuarios")
def listar_usuarios():
    """Listar todos los usuarios"""
    try:
        response = requests.get(f"{API_URL}/usuarios/")
        usuarios = response.json() if response.status_code == 200 else []
    except Exception:
        usuarios = []
        flash("Error al conectar con la API", "danger")
    return render_template("usuarios.html", usuarios=usuarios)


@app.route("/usuarios/crear", methods=["GET", "POST"])
def crear_usuario():
    """Crear un nuevo usuario"""
    if request.method == "POST":
        datos = {"nombre": request.form.get("nombre"), "correo": request.form.get("correo")}
        try:
            response = requests.post(f"{API_URL}/usuarios/", json=datos)
            if response.status_code == 200:
                flash("Usuario creado exitosamente", "success")
                return redirect(url_for("listar_usuarios"))
            else:
                flash(f"Error al crear usuario: {response.text}", "danger")
        except Exception as e:
            flash(f"Error al conectar con la API: {str(e)}", "danger")
    return render_template("crear_usuario.html")


@app.route("/canciones")
def listar_canciones():
    """Listar todas las canciones"""
    try:
        response = requests.get(f"{API_URL}/canciones/")
        canciones = response.json() if response.status_code == 200 else []
    except Exception:
        canciones = []
        flash("Error al conectar con la API", "danger")
    return render_template("canciones.html", canciones=canciones)


@app.route("/canciones/crear", methods=["GET", "POST"])
def crear_cancion():
    """Crear una nueva canción"""
    if request.method == "POST":
        datos = {
            "titulo": request.form.get("titulo"),
            "artista": request.form.get("artista"),
            "album": request.form.get("album"),
            "duracion": int(request.form.get("duracion")),
            "año": int(request.form.get("año")),
            "genero": request.form.get("genero"),
        }
        try:
            response = requests.post(f"{API_URL}/canciones/", json=datos)
            if response.status_code == 200:
                flash("Canción creada exitosamente", "success")
                return redirect(url_for("listar_canciones"))
            else:
                flash(f"Error al crear canción: {response.text}", "danger")
        except Exception as e:
            flash(f"Error al conectar con la API: {str(e)}", "danger")
    return render_template("crear_cancion.html")


@app.route("/favoritos")
def listar_favoritos():
    """Listar todos los favoritos"""
    try:
        response = requests.get(f"{API_URL}/favoritos/")
        favoritos = response.json() if response.status_code == 200 else []
    except Exception:
        favoritos = []
        flash("Error al conectar con la API", "danger")
    return render_template("favoritos.html", favoritos=favoritos)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
