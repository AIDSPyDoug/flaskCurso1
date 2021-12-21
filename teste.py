from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
    jogo2 = Jogo('Pokemon', 'RPG', 'GBA')
    jogo3 = Jogo('Age2', 'RTS', 'PC')
    lista =[jogo1, jogo2, jogo3 v]
    return render_template('lista.html', titulo='jogos', jogos=lista)
app.run()