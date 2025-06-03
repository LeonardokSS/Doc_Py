#Módulos: geralmente serve como uma distribuição de métodos/funções/etc em vários arquivos facilitando a escrita de um código.

#Definição de módulo(documentação pytho):

#Para permitir isso, Python tem uma maneira de colocar as definições em um arquivo e então usá-las em um script ou em uma execução interativa do interpretador. Tal arquivo é chamado de módulo; definições de um módulo podem ser importadas para outros módulos, ou para o módulo principal (a coleção de variáveis a que você tem acesso num script executado como um programa e no modo calculadora).

#Para se criar um arquivo basta: nome_do_módulo.py


#Exemplo de modulação:


def soma(x):
        return 10 + x

if __name__ == "__main__":
    import sys
    print(soma(int(sys.argv[1])))


#Jeitos de importar um módulo:

#import módulo = vai importar o módulo inteiro
#from módulo import método = vai importar do módulo um método específico
#from módulo import * = vai importar tudo do módulo específico
#import módulo as nome_novo_módulo = vai importar um módulo com um outro nome específico
#from módulo import método as nome_novo_método = vai importar um método específico com um outro nome específico

#if __name__ = "__main__": possibilita a passagem de argumentos no prompt do terminal

#diretório __pycache__: serve para possibilitar o uso de cache com módulo, permitindo ser mais rápido, o arquivo em cache geralmente tem a forma de: nome_arquivo.pyc

#O Python traz uma biblioteca padrão de módulos, descrita em um documento em separado, a Referência da Biblioteca Python (doravante “Referência da Biblioteca”). Alguns módulos estão embutidos no interpretador; estes possibilitam acesso a operações que não são parte do núcleo da linguagem, mas estão no interpretador seja por eficiência ou para permitir o acesso a chamadas do sistema operacional. O conjunto destes módulos é uma opção de configuração que depende também da plataforma utilizada. Por exemplo, o módulo winreg só está disponível em sistemas Windows. Existe um módulo que requer especial atenção: sys, que é embutido em qualquer interpretador Python. 

#dir() = serve para retornar os nomes disponíveis em um módulo, sem um argumento(módulo), ele passa os argumentos atualmente definidos 

#verificar soma.py

