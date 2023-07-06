import socket

server_ip = '192.168.0.53'  # ip da maquina no servidor
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))

    server_socket.listen(1)
    print("Servidor pronto para receber conexões.")

    client_socket, client_address = server_socket.accept()
    print("Conexão estabelecida com:", client_address)

    while True:
        message = client_socket.recv(1024).decode()
        print("String recebida:", message)

        valor_selecionado = int(message)  # Converter a mensagem em um número inteiro

        matriz = [[0] * 4 for _ in range(6)]  # Inicializar a matriz 6x4 com zeros
        total_1s = min(valor_selecionado, 24)  # Limitar o total de 1s à dimensão da matriz

        for i in range(total_1s):
            linha = 5 - (i // 4)  # Calcular o índice da linha de baixo para cima
            coluna = i % 4  # Calcular o índice da coluna
            matriz[linha][coluna] = 1

        # Imprimir a matriz
        for linha in matriz:
            print(linha)

        modified_message = message.upper()

        client_socket.send(modified_message.encode())

finally:
    # O código do servidor não fecha a conexão
    server_socket.close()
