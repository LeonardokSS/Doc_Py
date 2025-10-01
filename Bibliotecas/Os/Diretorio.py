import os

#Manipulação de diretorios, ou simplismente de caminhos de pastas.

os.getcwd()  ##Mostra o caminho da pasta atual

os.chdir('Teste1') #Muda para outra pasta

os.getcwd() #Mostra o caminho da pasta atual.

os.chdir('pasta') 	#Muda para outra pasta

os.listdir() 	#Lista os arquivos e pastas da pasta atual.

os.mkdir('Pasta_nova') #Cria uma nova pasta

os.makedirs('pasta/subpasta') #Cria uma pasta e as subpastas necessárias.

os.rmdir('pasta') 	#Apaga uma pasta vazia.

os.removedirs('pasta/subpasta')	#Todas as pastas nesse caminho serão apagadas