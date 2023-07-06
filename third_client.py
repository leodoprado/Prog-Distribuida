import socket

server_ip = '192.168.0.53'  # IP da máquina do servidor
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))
    print("Conexão estabelecida com o servidor.")

    while True:
        porcentagem = client_socket.recv(1024).decode()
        if not porcentagem:
            break
        print("Porcentagem de preenchimento da matriz:", porcentagem, "%")

finally:
    client_socket.close()