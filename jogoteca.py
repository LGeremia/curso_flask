from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

app.secret_key = 'teste'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

usuario1 =  Usuario('gere', 'Gere', 'teste')
usuario2 =  Usuario('teste', 'teste', 'teste2')
usuarios = {
    usuario1.id: usuario1,
    usuario2.id: usuario2
}

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('list.html', title='Jogos', jogos=lista)

@app.route('/new')
def new():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect(url_for('login',redirect=url_for('new')))
    return render_template('new.html', title='Novo Jogo')

@app.route('/create', methods=['POST',])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    next_page = request.args.get('redirect')
    return render_template('login.html',title='Login', next_page=next_page)

@app.route('/authenticate', methods=['POST',])
def authenticate():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        print('aqui')
        if usuario.password == request.form['senha']:
            next_page = request.form['next_page']
            session['usuario_logado']=usuario.id
            flash(usuario.username + ' logou com sucesso!')
            return redirect(next_page)
        else:
            flash('Usuário ou senha inválidos!')
            return redirect(url_for('login'))
    else:
        flash('Usuário ou senha inválidos!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout feito com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)