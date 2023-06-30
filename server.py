import socket

server_ip = '192.168.1.234' # ip da maquina no servidor
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))

    server_socket.listen(1)
    print("Servidor pronto para receber conexões.")

    while True:
        client_socket, client_adress = server_socket.accept()
        print("Conexão estabelecida com:", client_adress)

        message = client_socket.recv(1024).decode()
        print("String recebida:", message)

        modified_message = message.upper()

        client_socket.send(modified_message.encode())

        client_socket.close()
        print("Conexão encerrada com:", client_adress)

finally:
    server_socket.close()