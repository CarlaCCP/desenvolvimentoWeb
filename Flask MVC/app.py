from flask import Flask, render_template

app = Flask('teste')

LISTA = [
    "Item 1",
    "Item 2",
    "Item 3"
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ola')
def ola():
    resposta = '<h1>Olá mundo no Flask</h1>'
    
    resposta = resposta + '<ul>'

    for item in LISTA:
        resposta += '<li>' + item + '</li>' 
    
    resposta = resposta + '</ul>'
    
    return resposta


app.run(debug=True)