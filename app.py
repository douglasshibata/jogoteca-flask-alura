from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Joogo 1','Jogo 2 ','Jogo 3','Joogo 4']
    return render_template('lista.html',titulo='Jogos',jogos=lista)

app.run()
