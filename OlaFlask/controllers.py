from app import app
from flask import render_template, request




@app.route('/')
def home():
   
    return render_template('index.html' , titulo = "Testando tag")

@app.route('/ola')
def ola():
    return render_template('ola.html')

@app.route('/form', methods=['GET', 'POST'])
def formularios():
    if request.method == 'POST':
        print("Isto é um POST feito por", request.form['nome'])
    else:
        print("Isto é um GET")
    return render_template('formulario.html')