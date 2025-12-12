import psutil

print("=== MONITORAMENTO DO SISTEMA ===")

cpu = psutil.cpu_percent(interval=1)
mem = psutil.virtual_memory()

print(f"Uso de CPU: {cpu}%")
print(f"Uso de RAM: {mem.percent}%")
print(f"RAM usada: {mem.used / (1024**3):.2f} GB")
print(f"RAM total: {mem.total / (1024**3):.2f} GB")
