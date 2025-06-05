#match case precisa apenas de uma variavel para funcionar.

status = (input("Digite seu erro:"))
def erros(status):
    match status:
        case 1:
            return "Erro de conexão"
        case 2:
            return "Erro syntaxe"
        case 3:
            return "Foi mal dormi"
        case _:
            return "Desista da sua vida"
            




