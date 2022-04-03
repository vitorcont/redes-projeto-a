import sys
import socket
from datetime import datetime
import pytz

port_aux = False

print('DIGITE O IP DO SERVER: ')
ip = input()
print('DIGITE A PORTA: ')
port = int(input())

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destiny = (ip, port)

tz_SP = pytz.timezone('America/Sao_Paulo')
datetime_SP = datetime.now(tz_SP)

print('CONECTADO AO CHAT!')
print('ENVIE SUA MENSAGEM!\n')
while True:
    msg = input()
    current_time = datetime_SP.strftime("%H:%M:%S")

    json = {
        'Ip_Origem': socket.gethostbyname(socket.gethostname()),
        'Ip_Destino': ip,
        'Porta_Origem': udp.getsockname()[1] if port_aux == False else 8080,
        'Porta_Destino': port,
        'Timestamp': current_time,
        'Mensagem': msg
    }
    udp.sendto(bytes(str(json), "utf8"), destiny)
    port_aux = True

    # Ack
    msg_recv_ack, end_client_ack = udp.recvfrom(1024)
    print(f"Ack {end_client_ack}: ", msg_recv_ack.decode('utf-8'), '\n')

    # Timestamp de recebimento
    msg_recv, end_client = udp.recvfrom(1024)
    print(f"Server {end_client}: ", msg_recv.decode('utf-8'))

udp.close()
