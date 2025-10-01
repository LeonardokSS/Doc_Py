import os

os.remove('arquivo.txt') #Apaga um arquivo

os.rename('Me_apague.txt') #Mudo o nome do arquivo

os.replace('Me_apague.txt','Novo.txt') #Substitui o arquivo por um novo

os.stat('Me_apague.txt') #Retorna todas as informações sobre o arquivo

os.path.getsize('caminho')	#Retorna o tamanho de um arquivo em bytes.

os.path.getmtime('caminho')	#Retorna a data da última modificação.




