import os

#Executa comando dentro do CMD
  #Comando super util para limpar as mensagens do CMD
os.system('cls') #Executa um comando no sistema

os.startfile('Brave.exe') #Executa qualquer arquivo



#Executa verificações de informações dentro do sistema, como o nome.
   # Win = nt / Lix = posix /
nome = os.name
print(os.name)

usuario = os.getlogin()	#Mostra o nome do usuário.
print(usuario)

# Mostra quantos núcleos de CPU existem
cpus = os.cpu_count()
print(f"Número de CPUs: {cpus}")

# Mostra o ID do programa atual
pid = os.getpid()
print(f"ID do programa atual: {pid}")

# Mostra o ID do programa "pai"
ppid = os.getppid()
print(f"ID do processo pai: {ppid}")
