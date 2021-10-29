# Aula 11 - Cookies

from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        dados = request.form['c']
        resp.set_cookie('teste_cookie', dados)

    return resp


@app.route('/getcookie')
def getcookie():
    cookie_name = request.cookies.get('teste_cookie')
    return f'<h1>Valor cookie é: {cookie_name}</h1>'


if __name__ == '__main__':
    app.run(debug=True)
