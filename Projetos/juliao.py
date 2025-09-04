import speech_recognition as sp
import time

#Definir uma variavel para armazenar a classe recognizer
reconhecer = sp.Recognizer()
max_vezes = 2


VEZES = 0 


def reconhecer_voz():
   
   global VEZES

   while True:
    if VEZES > max_vezes:
      print("Muitas tentativas falhas. Reiniciando sistemas em 10 segundos...")
      time.sleep(10)
      VEZES = 0  
      return reconhecer_voz() 
   #Definir o caminho de onde o codigo ira escutar o audio
    with sp.Microphone() as source:
     print("Me diga seu nome!")
     #Metodo para medir o barulho ambiente por 2 segundos , fazer uma média e depois com isso ele pode saber oque é a voz 
     reconhecer.adjust_for_ambient_noise(source, duration = 2)
     time.sleep(0.5)
     #Variavel para armazenar o audio
     audio = reconhecer.listen(source)
    #Enviar texto para API do google para transformar o audio em texto 
     try:
       audio = reconhecer.recognize_google(audio, language="pt-BR")
       print(f"Você disse: {audio}? ")
       resposta = input("Responda se estou certo ou não?")
       if resposta == "Sim":
         print ("Ok vamos continuar")
         break
       elif resposta == "Não":
         print("OK, vamos tentar novamente")
       time.sleep(5)
       
     except sp.UnknownValueError:
       VEZES += 1
       print(f"Não entendi, fale novamente! Essa e sua tentativa:{VEZES}")

       return reconhecer_voz()
     except sp.RequestError:
       print("Erro ao concectar ao serviço, por favor volte mais tarde!")
       return None


if __name__ == "__main__":
  reconhecer_voz()
