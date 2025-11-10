import keyboard
import time

def Power():
    keyboard.press_and_release('windows')
    time.sleep(0.5)
    keyboard.write("power")
    time.sleep(0.5)
    keyboard.press_and_release('right')
    time.sleep(0.5)
    keyboard.press_and_release('down')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(0.5)


def chris():
    Power()
    time.sleep(0.5)
    keyboard.write("iwr -useb https://christitus.com/win | iex")
    time.sleep(0.5)
    keyboard.press_and_release('enter')

def removerApps(i):
    Power()
    match i:
        case "Edge":
            # Comando correto para remover o Microsoft Edge
            keyboard.write("Get-AppxPackage *Microsoft.MicrosoftEdge* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
        case "OneDrive":
            # Comando correto para remover o OneDrive
            keyboard.write("Get-AppxPackage *OneDrive* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
        case "Xbox":
            # Comando correto para remover o Xbox Game Bar
            keyboard.write("Get-AppxPackage *Microsoft.XboxGamingOverlay* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
        case "Cortana":
            # Comando correto para remover a Cortana
            keyboard.write("Get-AppxPackage *Microsoft.Cortana* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
        case "Todos":
            # Remover todos os apps de uma vez
            keyboard.write("Get-AppxPackage *OneDrive* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
            time.sleep(0.2)
            keyboard.write("Get-AppxPackage *Microsoft.XboxGamingOverlay* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
            time.sleep(0.2)
            keyboard.write("Get-AppxPackage *Microsoft.Cortana* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
            time.sleep(0.2)
            keyboard.write("Get-AppxPackage *Microsoft.MicrosoftEdge* | Remove-AppxPackage")
            time.sleep(0.2)
            keyboard.press_and_release("enter")
print("Otimização finalizada!")


while True:
    print("=== Sistema Otimização ===")
    input = int(input("1 - Acessar o PowerShell(CTT)"))

    match input:
        case 1:
            chris()
        case 2:   
            i = input("Digite o nome do app que voce deseja excluir \n" \
            "Edge\n" \
            "OneDrive\n" \
            "Xbox\n" \
            "Cortana\n" \
            "Todos")
            removerApps(i)
            
