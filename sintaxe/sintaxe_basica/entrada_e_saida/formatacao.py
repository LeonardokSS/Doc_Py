#Até agora vimos 2 métodos simples para escrever saída: print() e expressões

#Existem várias maneira de formatar a saída, por exemplo:

nome = 'Gustavo'
anos = '16'
cidade = 'São Paulo'

print(f'Meu nome é {nome} eu tenho {anos} moro em {cidade}')

#Também podemos usar o métood str.format() para formatar uma string

print('{} gosta de ler'.format(nome))
print('{} tem {} anos e mora em {}'.format(nome,anos,cidade))

#Existe uma Minilinguagem de formatação para format

#Exemplos:

print ('{}, {}, {}'.format('a','b','c')) #Deixando por padrão
print ('{1}, {2}, {0}'.format('a','b','c')) #Mudando as posições da formatação
print ('{}, {}, {}'. format(*'abc')) #Descompactando a formatação
print ('{0}{1}{2}, {2}{1}{0}, {1}{2}{0}'.format('a','b','c')) #Também é possível concatenar formatação

x = 10-3j

print('{0.real}, {0.imag}, {0}'.format(x)) #Acessando atributos de formatação

lista = [1,2,3,4,5]

print('{0[0]}, {0[1]}, {0[2]}, {0[4]}'.format(lista)) #Acessando os itens da formatação

print('{!r}, {!s}'.format('palavra', 'palavra')) #Acrescentando ''

print('{:<30}'.format('alinhado a esquerda')) #alinha a esquerda
print('{:>30}'.format('alinhado a direita')) #alinha a direita
print('{:^30}'.format('Centralizado')) #deixa centralizado
print('{:*^30}'.format('Usa * como preenchimento')) #preenche com um caractere especial



print('O número {:+f} é positivo'.format(10)) #Mostra um sinal positivo
print('O número {:f} é negativo'.format(-10)) #Mostra um sinal negativo
print('O número {:f} tem qual sinal? '.format(10)) #Mostra apenas o sinal


print('O número {:,} tem quantas casas decimais'.format(123456789)) #separa as casas decimais com ,

print('Dea sempre seu {:.1%}'.format(1)) #Multiplica por cem e coloca porcentagem no final

print('String com \'!a\': {!a}'.format('Bem vindo')) #Em si faz a mesma coisa que o !r, porém usa o método ascii()

# a = 'letra a'
# b = 'letra b'
 
# print('A {} e a {} são legais'.format(a=, b=)) #Só pode ser usado em python 3.14. Coloca um sinal de igual no final



