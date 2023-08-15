from flask import Flask, render_template, request, redirect

class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
        
jogo1= Jogo('Tetris','Puzzle','Atarri')
jogo2= Jogo('God of war','Rock','PS2')
jogo3= Jogo ('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1,jogo2,jogo3]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/inicio')
def ola():

    return render_template('lista.html',titulo='Jogos',jogos=lista)



@app.route('/apostilas')
def apostilas_online():
# inicio do trecho Python
    lista_apostilas = ['HTML, CSS e Javascript', 'Java para Web']
    return render_template('apostilas.html', lista=lista_apostilas)

# fim trecho


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')





app.run(debug = True)