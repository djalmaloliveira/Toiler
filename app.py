from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return 'Ola Djalma3 !!'


@app.route("/aluno")
def aluno():
    return 'Aqui é o aluno2 !!'



if __name__ == "__main__":
    app.run(debug=True)