#Para criar um loop while, basta: while(condição): comando

i = 0
while True:
    print('True')
    i = i + 1
    if(i == 10):
        break

i = 10


while(i > 5):
    print('I maior que 5')
    i = i - 1
    if(i == 5):
        break
    
#A instrução pass não faz nada. Pode ser usada quando a sintaxe exige uma instrução, mas a semântica do programa não requer #nenhuma ação.

a = 20
while(a > 10): 
    if(a != 20):
        pass # pass usado para 'continuar' a ação
    a = a -1
    print('Valor de a: ', a)

while True: #esperando algo acontecer (interrupção de teclado)
    pass
    