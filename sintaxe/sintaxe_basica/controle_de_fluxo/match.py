#Uma instrução match é equivalente a uma instrução switch/case em uma linguagem de programação convencional para fazer isso basta: match(variável_analisada): case valor_da_variável: comando case valor_da_variável: comando

digito = int(input('Digite um número: '))

match digito:
    case 1:
        print('O número é 1')
    case 2: 
        print('O número é 2')
    case 3: 
        print('O número é 3')
    case 4 | 5 | 6:
        print('O número é ou 4 ou 5 ou 6')
