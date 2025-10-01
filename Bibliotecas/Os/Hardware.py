import os
import platform
import psutil

def get_hardware_info():
    print("=== Informações do Sistema ===")
    print(f"Sistema: {platform.system()} {platform.version()}")
    print(f"Processador: {platform.processor()}")
    print(f"Arquitetura: {platform.machine()}")
    
    # CPU
    print("\n=== CPU ===")
    print(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
    print(f"Núcleos totais: {psutil.cpu_count()}")
    print(f"Uso atual CPU: {psutil.cpu_percent()}%")
    
    # Memória
    mem = psutil.virtual_memory()
    print("\n=== Memória ===")
    print(f"Total: {mem.total / (1024**3):.2f} GB")
    print(f"Disponível: {mem.available / (1024**3):.2f} GB")
    print(f"Em uso: {mem.percent}%")
    
    # Disco
    disk = psutil.disk_usage('/')
    print("\n=== Disco ===")
    print(f"Total: {disk.total / (1024**3):.2f} GB")
    print(f"Livre: {disk.free / (1024**3):.2f} GB")
    print(f"Em uso: {disk.percent}%")

if __name__ == "__main__":
    get_hardware_info()