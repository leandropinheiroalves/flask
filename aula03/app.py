# Aula 03 - Criando URL Dinâmicas

from flask import Flask

app = Flask(__name__)


@app.route('/hello')
@app.route('/hello/<nome>')
def hello(nome=''):
    return f'<h1>Hello {nome}</h1>'


@app.route('/blog/')
@app.route('/blog/<int:postid>')
def blog(postid=-1):
    if postid >= 0:
        return f'Blog info {postid}'
    else:
        return 'Blog Todo'


@app.route('/blog/<float:postid>')
def blog2(postid=-1):
    if postid >= 0:
        return f'Blog info {postid}'
    else:
        return 'Blog Todo'


if __name__ == '__main__':
    app.run(debug=True)
