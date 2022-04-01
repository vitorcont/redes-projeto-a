import sys
import socket
from datetime import datetime
import pytz

port_aux = False

ip = sys.argv[1]
port = int(sys.argv[2])

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destiny = (ip, port)

tz_SP = pytz.timezone('America/Sao_Paulo')
datetime_SP = datetime.now(tz_SP)

while True:
    msg = input()
    current_time = datetime_SP.strftime("%H:%M:%S")

    json = {
        'Ip_Origem': socket.gethostbyname(socket.gethostname()),
        'Ip_Destino': ip,
        'Porta_Origem': udp.getsockname()[1] if port_aux = False else 8080,
        'Porta_Destino': port,
        'Timestamp': current_time
        'Mensagem': msg
    }
    udp.sendto(bytes(msg, "utf8"), destiny)

    port_aux = True

    msg_recv, end_client = udp.recvfrom(1024)
    # Timestamp de recebimento
    current_time = datetime_SP.strftime("%H:%M:%S")
    print("Recebi = ", msg_recv, " , Do cliente",
          end_client, ' Timestamp Resposta: ', current_time)

udp.close()
