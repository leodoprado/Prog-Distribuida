import socket
import time

server_ip = '192.168.192.95'  # IP da máquina do servidor
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
        print("Qtd de lixo inserido:", modified_message)

        # Verificar se a matriz foi zerada no servidor
        if modified_message == "LIMPEZA_CONCLUIDA":
            print("O caminhão chegou para a coleta.")
            valor = 0  # Reiniciar o valor para 1

        valor += 1

        time.sleep(1)  # Atraso de 2 segundos entre os envios

        # Verificar se foi recebido o comando para zerar a matriz e reiniciar o loop
        if modified_message == "LIMPEZA_CONCLUIDA":
            time.sleep(2)
            print("Aguardando o carregamento dos resíduos.")
            time.sleep(4)
            print("Limpeza 100% concluída!")
            valor = 0  # Reiniciar o valor para 1

finally:
    client_socket.close()
