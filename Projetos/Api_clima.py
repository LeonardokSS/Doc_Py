import requests as rq
import json
#Chave da Api
chave = "7e7f140038d14ff44e53ba8feab0b659"

#Cidade para verificar
cidade = input("Digite o nome da cidade que você deseja consultar: ")

#Url da requisição
url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric&lang=pt_br"


#Variavel para armazenar o valor dos dados
requerirClima = rq.get(url)

#Transoformar os dados em JSON
Dados = requerirClima.json()

print(Dados)

temp = Dados["main"]["temp"]
desc = Dados["weather"][0]["description"]
umidade = Dados["main"]["humidity"]


print(f"A temperatura da cidade {cidade} é {temp} C\nO tempo está:{desc}\nA umidade é {umidade}%")

