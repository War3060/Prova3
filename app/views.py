from flask import render_template
from app import app 

@app.route('/')
def home():
    return "<b>There has been a change1</b>"

@app.route('/template')
def template():
    return render_template('home.html')



@app.route('/hora')
def hora():
    from datetime import datetime
    return f'O horario atual do sevidor é: {datetime.now()}' 
    
@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1=5, n2=7): 
    return f'A soma entre {n1} e {n2} é igual a {n1+n2}'
