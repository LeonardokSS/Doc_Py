from flask import Flask, request

app = Flask(__name__)

#Utilizando o method post podemos processar informações de um jeito mais seguro sem aparecer na URL

# Para criar uma rota com post precisamos definir os parametros


@app.route('/', methods=['get'])
def formulario():
    return '''
        <form action="/nome" method="post">
            Digite seu nome: <input type="text" name="nome">
            <input type="submit" value="Enviar">
        </form>
    '''

# Rota que recebe o as informações do formulario
@app.route('/nome', methods=['POST'])
def mostrar_nome():
    nome = request.form.get('nome')
    return f"<p>Seu nome registrado é {nome}</p>"


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        return f"Olá, {nome}!"
    return '''
        <form method="post">
            Nome: <input type="text" name="nome">
            <input type="submit">
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)
