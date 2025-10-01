#Importação dos modulos de flask e request
from flask import Flask, request


#Cria uma aplicação no flask
app = Flask(__name__)



#Rota principal que pega um get com um formulário html
@app.route('/')
def home():  # Ele basicamente pega o nome por meio do input e depois podemos pegar ele pelo name = "nome"
    return '''
        <form action="/nome">      
            Digite seu nome: <input type="text" name="nome">
            <input type="submit">
        </form>
           '''


#Depois de dar o submit a aplicação ira para a rota nome
@app.route('/nome')
def mostrarnome():  #Logo o valor do "nome sera pego pelo request dentro do html"
    nome = request.args.get('nome')
    #depois ele retornara formatado 
    return f"<p> Seu nome é {nome}</p>"



#inicia a aplicação
if __name__ == '__main__':
    app.run(debug=True)
