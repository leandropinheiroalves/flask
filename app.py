# Aula 01 - Instalação
# Aula 02 - Criando Rotas e configurações
# Aula 03 - Criando URL Dinâmicas
# Aula 04 - Construção de URL

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def admin():
    return '<h1>Admin<h1>'


@app.route('/guest/<name>')
def guest(name):
    return f'<p>Olá guest <b>{name}</b></p>'


@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', name=name))


if __name__ == '__main__':
    app.run(debug=True)