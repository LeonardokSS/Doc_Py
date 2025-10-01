#Importação dos modulos de flask e request
from flask import Flask, request


#Cria uma aplicação no flask
app = Flask(__name__)



#Rota básica para apenas mostrar Olá
@app.route('/mostrar_ola')
def mostrar():
    return f"Olá"

#Rota para pegar o nome por um formulario e assim que ele pegar com o submit, o navegador ira fazer um get para a rota /nome mostrando o nome
@app.route('/')
def pegar_nome():
    return '''
            <form action="/nome">      
                Digite seu nome: <input type="text" name="nome">
                <input type="submit">
            </form>
            '''

#Rota que o navegador faz a requisição assim que a pessoa apertar o botão do submit
@app.route('/nome')
def mostrar_nome():
     nome = request.args.get('nome')
     return f"O seu nome registrado é {nome}"




#inicia a aplicação
if __name__ == '__main__':
    app.run(debug=True)




