funcionarios = []
campos = ["nome","produtividade","colaboracao","pontualidade","media","classificacao"]
 
def classificar(media):
    if media > 10 or media < 0:
        return "Nota inválida"
    elif 9.0 <= media <= 10.0:
        return "Excelente"
    elif 7.0 <= media < 9.0:
        return "Bom"
    elif 5.0 <= media < 7.0:
        return "Regular"
    else:  
        return "Insuficiente"
 
arredondar = lambda x: round(x, 3)
 
def calcular_media(p, c, pn):
    return (p + c + pn) / 3
 
while True:
    nome = input("Nome do funcionário (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
 
    try:
        produtividade = float(input("Nota de produtividade: "))
        colaboracao = float(input("Nota de colaboração: "))
        pontualidade = float(input("Nota de pontualidade: "))
    except ValueError:
        print("Digite um número válido!")
        continue
 
    media_calc = calcular_media(produtividade, colaboracao, pontualidade)
    media_arredondada = arredondar(media_calc)
    classificacao = classificar(media_arredondada)
 
    funcionario = {
        campos[0]: nome,
        campos[1]: produtividade,
        campos[2]: colaboracao,
        campos[3]: pontualidade,
        campos[4]: media_arredondada,
        campos[5]: classificacao
    }
 
    funcionarios.append(funcionario)
 
funcionarios_ordenados = sorted(funcionarios, key=lambda f: f["media"], reverse=True)
 
print("\n===== DADOS NA ORDEM INSERIDA =====")
print(f"{'NOME':<15}{'MÉDIA':<10}{'CLASSIFICAÇÃO':<15}")
print("-" * 45)
for f in funcionarios_ordenados:
    print(f"{f['nome']:<15}{f['media']:<10}{f['classificacao']:<15}")
 