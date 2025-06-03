#Diferente de sequências que são indexadas por inteiros, dicionários são indexados por chaves (keys), que podem ser de qualquer tipo imutável (como strings e inteiros). Tuplas também podem ser chaves se contiverem apenas strings, inteiros ou outras tuplas. Se a tupla contiver, direta ou indiretamente, qualquer valor mutável, não poderá ser chave. Listas não podem ser usadas como chaves porque podem ser modificadas internamente pela atribuição em índices ou fatias, e por métodos como append() e extend(). 

#Trecho acima tirado da própria documentação do python

#Para se criar um dicionário basta: nome_dic = {chave:valor}

#Exemplo

dic = {'nome' : 'Gustavo', 'idade' : '16', 'cidade' : 'São Paulo', 'gênero':'Masculino'}

#list(d) = devolve a lista de todas as chaves presentes no dicionário

print('Verificando as chaves com list :', list(dic))

#sorted(d) = devolve a lista de todas as chaves em ordem

print('Verificando as chaves com sorted : ', sorted(dic))

#in = verifica se a presença de chaves

print('gênero' in dic)

#dict() = constrói automáticamente um dicionário com chave:valor

dicionário = dict({'Título':'Dicionário', 'Páginas':'101'})

print('Verificando as chaves do novo dicionário com list : ', list(dicionário))

#items() = retorna a chave e o valor simultaneamente

print('Retornando as chaves e valores do dicionário dic em ordem, ', sorted(dic.items()))

#enumerate() = retorna o valor e a posiçãõ simultaneamente

print('Retornando os valores e as posições em ordem do dicionário dic, ', sorted(enumerate(dic)))

#zip() = percorre mais de um dicionário simultaneamente

print('Retornando as chaves e os valores do dicionário dic e do dicionário \'dicionario\'', sorted(zip(dic,dicionário)))

#reversed() = percorre o dicionário de forma inversa

dic_ordenado_inverso = {chave: dic[chave] for chave in reversed(dic)}
print('Dicionário na ordem inversa: ', dic_ordenado_inverso)

