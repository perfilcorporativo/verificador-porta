import psutil
import time
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def monitorar():
    while True:
        limpar_tela()

        cpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()

        print("=== MONITORAMENTO DO SISTEMA ===")
        print(f"Uso de CPU: {cpu}%")
        print(f"Uso de RAM: {memoria.percent}%")
        print(f"RAM usada: {round(memoria.used / (1024 ** 3), 2)} GB")
        print(f"RAM total: {round(memoria.total / (1024 ** 3), 2)} GB")
        print("\nPressione CTRL + C para sair")

        time.sleep(1)

if __name__ == "__main__":
    monitorar()
