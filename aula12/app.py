# Aula 12 - Session

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')





if __name__ == '__main__':
    app.run(debug=True)
