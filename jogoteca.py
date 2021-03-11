from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

app.secret_key = 'teste'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('list.html', title='Jogos', jogos=lista)

@app.route('/new')
def new():
    return render_template('new.html', titulo='Novo Jogo')

@app.route('/create', methods=['POST',])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticated', methods=['POST',])
def authenticated():
    if 'master' == request.form['senha']:
        session['usuario_logado']=request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash('Senha inválida!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout feito com sucesso!')
    return redirect('/')

app.run(debug=True)