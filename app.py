from flask import Flask, render_template

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
        


app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1= Jogo('Tetris','Puzzle','Atarri')
    jogo2= Jogo('God of war','Rock','PS2')
    jogo3= Jogo ('Mortal Kombat', 'Luta', 'PS2')
    lista = [jogo1,jogo2,jogo3]
    return render_template('lista.html',titulo='Jogos',jogos=lista)



@app.route('/apostilas')
def apostilas_online():
# inicio do trecho Python
    lista_apostilas = ['HTML, CSS e Javascript', 'Java para Web']
    return render_template('apostilas.html', lista=lista_apostilas)

# fim trecho
app.run()
