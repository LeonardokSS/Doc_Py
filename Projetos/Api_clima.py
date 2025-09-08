import requests as rq
import json
#Chave da Api
chave = "7e7f140038d14ff44e53ba8feab0b659"

#Cidade para verificar
Cidade = input("Digite o nome da Cidade que você deseja consultar: ")

#Url da requisição
Clima = f"http://api.openweathermap.org/data/2.5/weather?q={Cidade}&appid={chave}&units=metric&lang=pt_br"



#Variavel para armazenar o valor dos dados
requerirClima = rq.get(Clima)

#Transoformar os dados em JSON
Dados = requerirClima.json()

temp = Dados["main"]["temp"]

umidade = Dados["main"]["humidity"]

#Url para a Chuva
Chuva = f"https://api.openweathermap.org/data/2.5/forecast?q={Cidade}&units=metric&appid={chave}&lang=pt_br"


requirirChuva = rq.get(Chuva)

DadosChuva = requirirChuva.json()


Condicao = DadosChuva["list"][0]["weather"][0]["description"]
Chance = DadosChuva["list"][0]["pop"]

print(f"A situação atual é de: {Condicao}\nA chance de chuva é {Chance}%")


print(f"A temperatura da Cidade de {Cidade} é {temp} C\nA umidade é {umidade}%")
