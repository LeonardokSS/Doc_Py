import speech_recognition as sp
import time

#Definir uma variavel para armazenar a classe recognizer
reconhecer = sp.Recognizer()
max_vezes = 5

def reconhecer_voz():
   vezes = 0
   while max_vezes > vezes:
     
   #Definir o caminho de onde o codigo ira escutar o audio
    with sp.Microphone() as source:
     print("Me diga seu nome!")
     #Metodo para medir o barulho ambiente por 2 segundos , fazer uma média e depois com isso ele pode saber oque é a voz 
     reconhecer.adjust_for_ambient_noise(source, duration = 2)
     #Variavel para armazenar o audio
     audio = reconhecer.listen(source)
    #Enviar texto para API do google para transformar o audio em texto 
     try:
       audio = reconhecer.recognize_google(audio, language="pt-BR")
       print(f"Você disse: {audio}? ")
       print("Caso não clique no botão escrito abortar!")
       time.sleep(5)
     except sp.UnknownValueError:
       vezes += 1
       print(f"Não entendi, fale novamente! Essa e sua tentativa:{vezes}")

       return reconhecer_voz()
     except sp.RequestError:
       print("Erro ao concectar ao serviço, por favor volte mais tarde!")
       return None
     if max_vezes < vezes:
       print("Não consigo compreender você devido a ruidos externos, irei reiniciar!")
       time.sleep(20)
       return reconhecer_voz()

       
