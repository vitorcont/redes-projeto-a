import sys
import socket
from datetime import datetime
import pytz

ip = sys.argv[1]
port = int(sys.argv[2])

port_aux = False

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = (ip, port)
udp.bind(server)

tz_SP = pytz.timezone('America/Sao_Paulo')
datetime_SP = datetime.now(tz_SP)

while True:
    msg_recv, end_client = udp.recvfrom(1024)
    # Timestamp de recebimento
    current_time = datetime_SP.strftime("%H:%M:%S")
    print(f"Client {end_client}: ", msg_recv.decode('utf-8'), current_time)

    msg = input()

    current_time = datetime_SP.strftime("%H:%M:%S")

    json = {
        'Ip_Origem': ip,
        'Ip_Destino': end_client[0],
        'Porta_Origem': port,
        'Porta_Destino': udp.getsockname()[1] if port_aux != False else 8080,
        'Timestamp': current_time,
        'Mensagem': msg,
    }
    port_aux = True
    udp.sendto(bytes(str(json), "utf8"), end_client)
udp.close()
