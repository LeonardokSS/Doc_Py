import speech_recognition as sp
import time
import openai

# Configuração
openai.api_key = "<YOUR API KEY>"
reconhecer = sp.Recognizer()
max_vezes = 2

def reconhecer_voz():
    VEZES = 0
    while VEZES <= max_vezes:
        with sp.Microphone() as source:
            print("Me diga seu nome!")
            reconhecer.adjust_for_ambient_noise(source, duration=2)
            time.sleep(0.5)
            audio = reconhecer.listen(source)

        try:
            nome = reconhecer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {nome}?")
            resposta = input("Responda se estou certo ou não (Sim/Não): ")
            if resposta.lower() == "sim":
                print("Ok, vamos continuar")
                fase2(nome)
                return
            else:
                print("OK, vamos tentar novamente")
                VEZES += 1
        except sp.UnknownValueError:
            VEZES += 1
            print(f"Não entendi, fale novamente! Tentativa {VEZES}")
        except sp.RequestError:
            print("Erro ao conectar ao serviço, tente novamente mais tarde.")
            return

    print("Muitas tentativas falhas. Reiniciando em 10 segundos...")
    time.sleep(10)
    reconhecer_voz()

def fase2(nome):
    Tentativas = 0
    while Tentativas <= max_vezes:
        with sp.Microphone() as source:
            print(f"Ok {nome}, como você imagina o mundo perfeito?")
            reconhecer.adjust_for_ambient_noise(source, duration=2)
            time.sleep(0.5)
            audio = reconhecer.listen(source)

        try:
            mundo = reconhecer.recognize_google(audio, language="pt-BR")
            print(f"Então o mundo perfeito seria como: {mundo}?")
            resposta = input("Responda se estou certo ou não (Sim/Não): ")
            if resposta.lower() == "sim":
                print("Ok, gerando imagem...")
                response = openai.Image.create(
                    prompt=mundo,
                    n=1,
                    size="1024x1024"
                )
                image_url = response['data'][0]['url']
                print("Imagem gerada:", image_url)
                return
            else:
                Tentativas += 1
                print("OK, vamos tentar novamente")
        except sp.UnknownValueError:
            Tentativas += 1
            print(f"Não entendi, fale novamente! Tentativa {Tentativas}")
        except sp.RequestError:
            print("Erro ao conectar ao serviço, tente novamente mais tarde.")
            return

    print("Muitas tentativas erradas! Reiniciando em 10 segundos...")
    time.sleep(10)
    fase2(nome)

if __name__ == "__main__":
    reconhecer_voz()
