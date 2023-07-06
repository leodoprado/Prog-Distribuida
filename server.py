import socket

server_ip = '192.168.0.53'  # IP da máquina do servidor
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))

    server_socket.listen(2)  # Aumentar o número de conexões permitidas para 2

    print("Servidor pronto para receber conexões.")

    # Receber conexão do primeiro cliente
    client_socket, client_address = server_socket.accept()
    print("Conexão estabelecida com o primeiro cliente:", client_address)

    # Receber conexão do terceiro cliente
    truck_socket, truck_address = server_socket.accept()
    print("Conexão estabelecida com o terceiro cliente (caminhão):", truck_address)

    while True:
        message = client_socket.recv(1024).decode()
        print("String recebida:", message)

        if not message:
            break

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

        # Calcular a porcentagem de preenchimento da matriz
        porcentagem = (total_1s / 24) * 100

        # Verificar se a matriz está 100% preenchida
        if porcentagem == 100:
            print("Matriz 100% preenchida. Reinicializando...")
            matriz = [[0] * 4 for _ in range(6)]  # Zerar a matriz
            client_socket.sendall("MATRIZ_ZERADA".encode())

        # Enviar a porcentagem para o terceiro cliente (caminhão)
        truck_socket.sendall(f"{porcentagem}%".encode())

        modified_message = message.upper()

        client_socket.send(modified_message.encode())

finally:
    # Fechar as conexões
    server_socket.close()
    client_socket.close()
    truck_socket.close()