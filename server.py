import sys
import socket
# import json
# from datetime import datetime
# import pytz

ip = sys.argv[1]
port = int(sys.argv[2])


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = (ip, port)
udp.bind(server)

# ipOrigem = ip
# ipDestino = ip(?)
# portOrigem = udp.getsockname()[1]
# portDestino = port
# ----------------------------------------------
# TimestampOrigem e Destino:
# tz_SP = pytz.timezone('America/Sao_Paulo')
# datetime_SP = datetime.now(tz_SP)

# current_time = datetime_SP.strftime("%H:%M:%S")

while True:
    msg_recv, end_client = udp.recvfrom(1024)
    print(f"Client {end_client}: ", msg_recv.decode('utf-8'))

    msg = input()
    udp.sendto(bytes(msg, "utf8"), end_client)
    udp.sendfile('./teste.json', offset=0, count=1)
udp.close()
