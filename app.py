from flask import Flask, render_template, request, redirect, session, flash,url_for

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
app.secret_key = 'alura'

@app.route('/')
def index():
    return redirect(url_for('index'))

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
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('novo.html', titulo='Novo Jogo')
@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return redirect(url_for('login', proxima=url_for('novo')))

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logado.')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')


app.run(debug=True)