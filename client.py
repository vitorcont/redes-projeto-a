import sys
import socket

ip = sys.argv[1]
port = int(sys.argv[2])           

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destiny = (ip, port) 

while True:
	msg = input()             
	udp.sendto(bytes(msg,"utf8"), destiny)

	msg_recv, end_client = udp.recvfrom(1024)
	print ("Recebi = ",msg_recv," , Do cliente", end_client)
udp.close()
