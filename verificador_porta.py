import socket

def verificar_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    try:
        resultado = sock.connect_ex((host, porta))

        if resultado == 0:
            print(f"🔓 Porta {porta} ABERTA em {host}")
        else:
            print(f"🔒 Porta {porta} FECHADA em {host}")

    except Exception as e:
        print(f"❌ Erro ao verificar: {e}")

    finally:
        sock.close()


print("===== Verificador de Porta =====")
host = input("Digite o endereço IP ou site: ")
porta = int(input("Digite a porta que deseja verificar: "))

verificar_porta(host, porta)
