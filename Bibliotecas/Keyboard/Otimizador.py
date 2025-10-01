import keyboard
import time
import sys

def carregando():
    for i in range(21):
        barra = "#" * i + "-" * (20 - i)
        sys.stdout.write(f"\r[{barra}] {i*5}%")
        sys.stdout.flush()
        time.sleep(0.4)

def parar_func():
    global ver
    print("\nOperação parada!")
    ver = False

keyboard.add_hotkey('esc', parar_func)

Confirmacao = input("========== DESEJA COMEÇAR? ==========\n[1] - SIM\n[2] - NÃO\n")

ver = True

while ver:
    if Confirmacao == "1":
        carregando()
        keyboard.press_and_release('win+r')
        keyboard.write('cleanmgr')
        keyboard.press_and_release('enter')
        time.sleep(1)
        for _ in range(4):
            keyboard.press_and_release('enter')
            time.sleep(1)
        time.sleep(10)
        keyboard.press_and_release('win+r')
        time.sleep(0.7)
        keyboard.press_and_release('enter')
        time.sleep(0.7)
        keyboard.press_and_release('tab')
        time.sleep(0.7)
        keyboard.press_and_release('tab')
        time.sleep(0.7)
        keyboard.press_and_release('down')
        time.sleep(0.7)
        keyboard.press_and_release('enter')
        time.sleep(0.7)
        keyboard.press_and_release('enter')

        print("\nProcedimento Finalizado")
        break
      
    elif Confirmacao == "2":
        print('Cancelando operação')
        break
