import socket
import time

server_ip = '192.168.0.53'  # IP da máquina do servidor
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
    print("Conexão estabelecida com o servidor.")

    valor = 1
    while True:
        message = str(valor)

        client_socket.sendall(message.encode())

        modified_message = client_socket.recv(1024).decode()
        print("String modificada:", modified_message)

        # Verificar se a matriz foi zerada no servidor
        if modified_message == "MATRIZ_ZERADA":
            print("Matriz zerada. Reiniciando o loop.")
            valor = 1  # Reiniciar o valor para 1

        valor += 1

        time.sleep(3)  # Atraso de 3 segundos entre os envios

except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor.")

finally:
    client_socket.close()
