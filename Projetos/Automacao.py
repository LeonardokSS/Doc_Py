import subprocess
import keyboard
import time
import os
import sys

# =====================================================
# EXECUTAR POWERSHELL
# =====================================================

def run_ps(script):
    subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-Command", script],
        shell=True
    )

# =====================================================
# CHRIS TITUS TOOL (ÚNICO USO DE KEYBOARD)
# =====================================================

def chris_titus():
    keyboard.press_and_release('windows')
    time.sleep(0.5)
    keyboard.write("powershell")
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+shift+enter')
    time.sleep(1)
    keyboard.press_and_release('left')  # UAC
    time.sleep(0.3)
    keyboard.press_and_release('enter')
    time.sleep(1)

    keyboard.write("iwr -useb https://christitus.com/win | iex")
    time.sleep(0.3)
    keyboard.press_and_release("enter")

# =====================================================
# REMOVER APPS INÚTEIS
# =====================================================

def remover_apps():
    ps = r'''
$apps = @(
    "Microsoft.MSPaint",
    "Microsoft.MicrosoftStickyNotes",
    "Microsoft.SkypeApp",
    "Microsoft.GetHelp",
    "Microsoft.Getstarted",
    "Microsoft.MixedReality.Portal",
    "Microsoft.People",
    "Microsoft.WindowsFeedbackHub",
    "Microsoft.BingWeather",
    "Microsoft.BingNews"
)

foreach ($app in $apps) {
    Get-AppxPackage -Name $app -AllUsers | Remove-AppxPackage -ErrorAction SilentlyContinue
}
'''
    run_ps(ps)

# =====================================================
# DESATIVAR SERVIÇOS INÚTEIS
# =====================================================

def desativar_servicos():
    ps = r'''
$services = @(
    "DiagTrack","dmwappushservice","CDPSvc","WerSvc",
    "Fax","RetailDemo","RemoteRegistry","MapsBroker","lfsvc","PushToInstall",
    "Spooler","WSearch","TabletInputService","WbioSrvc"
)

foreach ($service in $services) {
    Stop-Service -Name $service -Force -ErrorAction SilentlyContinue
    Set-Service -Name $service -StartupType Disabled -ErrorAction SilentlyContinue
}
'''
    run_ps(ps)

# =====================================================
# OTIMIZAÇÃO PARA JOGOS (BAIXA LATÊNCIA)
# =====================================================

def otimizar_games():
    ps = r'''
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" SystemResponsiveness -Value 0

Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" "GPU Priority" -Value 8
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" "Priority" -Value 6
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" "Scheduling Category" -Value "High"
Set-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" "SFIO Priority" -Value "High"

powercfg -setactive SCHEME_MIN

powercfg -SETACVALUEINDEX SCHEME_CURRENT SUB_USB USBSELECTIVE SUSPEND 0
powercfg -SETDCVALUEINDEX SCHEME_CURRENT SUB_USB USBSELECTIVE SUSPEND 0
powercfg -setactive SCHEME_CURRENT

Set-ItemProperty "HKCU:\Control Panel\Mouse" MouseSpeed -Value 0
Set-ItemProperty "HKCU:\Control Panel\Mouse" MouseThreshold1 -Value 0
Set-ItemProperty "HKCU:\Control Panel\Mouse" MouseThreshold2 -Value 0

New-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows" -Name "GameDVR" -Force | Out-Null
Set-ItemProperty "HKLM:\SOFTWARE\Policies\Microsoft\Windows\GameDVR" AllowGameDVR -Value 0

netsh int tcp set global autotuninglevel=disabled
netsh int tcp set global ecncapability=disabled
netsh int tcp set global timestamps=disabled
netsh int tcp set global rss=enabled
netsh int tcp set global chimney=enabled
'''
    run_ps(ps)

# =====================================================
# MENU
# =====================================================

def menu():
    while True:
        os.system("cls")
        print("""
========================================
   WINDOWS OPTIMIZER - MENU PRINCIPAL
========================================
1 - Chris Titus Tool
2 - Remover aplicativos inúteis
3 - Desativar serviços inúteis
4 - Otimização para jogos (baixa latência)
5 - Executar TUDO
0 - Sair
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            chris_titus()
            input("Chris Titus Tool iniciado. Enter...")
        elif op == "2":
            remover_apps()
            input("Apps removidos. Enter...")
        elif op == "3":
            desativar_servicos()
            input("Serviços desativados. Enter...")
        elif op == "4":
            otimizar_games()
            input("Otimização gamer aplicada. Reinicie depois. Enter...")
        elif op == "5":
            remover_apps()
            desativar_servicos()
            otimizar_games()
            input("Tudo aplicado com sucesso. Reinicie o PC. Enter...")
        elif op == "0":
            sys.exit()
        else:
            input("Opção inválida. Enter...")

# =====================================================
# START
# =====================================================

if __name__ == "__main__":
    menu()
