#!/usr/bin/python -tt
import time
from flask import Flask, redirect, render_template, request
# Instancia de Flask. Aplicación
app = Flask(__name__, template_folder='template')


# Define la ruta principal
@app.route('/')
# Función para llamar a la página index.html
def index():
    return render_template("skincare.html")


# main del programa
if __name__ == "__main__":
    # Iniciamos la apicación en modo debug
    app.run(debug=True)
