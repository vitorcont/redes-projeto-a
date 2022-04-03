import sys
import socket
from datetime import datetime
import pytz
from ast import literal_eval

print('DIGITE O IP DO SERVER: ')
ip = input()
print('DIGITE A PORTA: ')
port = int(input())

port_aux = False

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (ip, port)
udp.bind(server)

tz_SP = pytz.timezone('America/Sao_Paulo')
datetime_SP = datetime.now(tz_SP)

while True:
    msg_recv, end_client = udp.recvfrom(1024)
    # Timestamp de recebimento
    current_recieved = datetime_SP.strftime("%H:%M:%S")
    print(f"Client {end_client}: ", msg_recv.decode('utf-8'))
    
    # send ack
    msg_recv = msg_recv.decode("utf8")
    msg_recv = literal_eval(msg_recv)
    msg_recv['Timestamp Resposta'] = current_recieved
    msg_recv['Ack'] = True
    udp.sendto(bytes(str(msg_recv), "utf8"), end_client)
    
    # response msg to client
    print('DIGITE O IP DO CLIENTE: ')
    ipclient = input()
    print('DIGITE A PORTA: ')
    portclient = int(input())
    msg = input()

    current_time = datetime_SP.strftime("%H:%M:%S")
    payload = {
        'Ip_Origem': ip,
        'Ip_Destino': ipclient,
        'Porta_Origem': port,
        'Porta_Destino': portclient,
        'Timestamp': current_time,
        'Mensagem': msg,
    }
    udp.sendto(bytes(str(payload), "utf8"), (ipclient,portclient))
udp.close()
