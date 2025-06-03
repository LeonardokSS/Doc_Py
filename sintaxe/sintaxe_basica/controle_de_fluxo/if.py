#Para criar comparações com a sentença if, basta usar:

#if(comparação):
    #comandos
#elif(else if, se precisar)(comparação):
    #comandos
#else: 

a = 5
b = 2

if (b < a):
    print(b , ' e menor do que: ' , a)
elif(a<b):
    print(a , ' e maior do que: ' , b)
else:
    print('Os dois números sao iguais')

#Operadores de comparação: >, <, !=, ==, >=, <=, 

# > = maior que
# < = menor que
# != diferente de
# == igual a
# >= maior ou igual
# <= menor ou igual


x = 10
y = 9
z = int(input('Digite um numero: '))

if (x == y) and (z > y):
    print('X é igual a Y, e Z é maior do que Y')
elif(x != y) and (z > y):
    print('X é diferente de Y, e Z é maior do que Y')
elif(x != z) or (z != y):
    print('X é diferente de Z, ou Z é diferente de y')
elif not x == y:
    print('X não é igual a y')


#Operadores lógicos: and, or, not

#and = se uma condição for verdadeira e a outra for verdadeira, verdadeiro: V,V = V
#and = se uma condição for verdadadeira e a outra for falsa, falso V,F = F
#and = se uma condição for falsa e a outra verdadeira, falso F,V = F
#and = se uma condição for falsa e a outra falsa, falso: F,F = F

#or = se uma condição for verdadeira e a outra for falsa, V,F = V
#or = se uma condição for verdadeira e a outra for verdadeira, V,V = V
#or = se uma condição for falsa e a outra for verdadeira, F,V = V
#or = se uma condição for falsa e a outra for falsa, F,F = F

#not = se a condição for verdadeira, V = V
#not = se a condição for falsa, F = F