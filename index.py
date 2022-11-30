#!/usr/bin/python -tt
# Importar Flask
import time
from flask import Flask, redirect, render_template, request
# Instancia de Flask. Aplicación
app = Flask(__name__, template_folder='template')


# Define la ruta principal
@app.route('/')
# Función para llamar a la página index.html
def index():
    return render_template("principal.html")
<<<<<<< HEAD



# Define la ruta principal Lucy Mosquera
@app.route('/LM')
# Función para llamar a la página index.html
def LM():
    return render_template("LM.html")


# Define la ruta principal Mercy Arrobo
@app.route('/MA')
# Función para llamar a la página index.html
def MA():
    return render_template("MA.html")

# Define la ruta principal Steveen Sinchiguano
@app.route('/SS')
# Función para llamar a la página index.html
def SS():
    return render_template("SS.html")

# Define la ruta principal Mary Guarnizo
@app.route('/MG')
# Función para llamar a la página index.html
def MG():
    return render_template("MG.html")

# Define la ruta principal Rachel Garces
@app.route('/RG')
# Función para llamar a la página index.html
def RG():
    return render_template("RG.html")
=======
>>>>>>> ab6e27bdfd72d5f7f56dee07dac443e589535637


# main del programa
if __name__ == "__main__":
    # Iniciamos la apicación en modo debug
    app.run(debug=True)
