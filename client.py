import socket
import time

server_ip = '192.168.0.53'  # ip da maquina que vai ser acessada
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

        valor += 1

        time.sleep(3)  # Atraso de 3 segundos entre os envios

except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor.")

finally:
    client_socket.close()