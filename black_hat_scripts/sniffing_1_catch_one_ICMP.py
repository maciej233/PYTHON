import socket
import os

host = '10.0.2.15'

# sprawwdzenie systemu operacyjnego nt = microsof
# posix = mac/linux
if os.name == 'nt':
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

# tworzymy obiekt
sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))

# przechwytujemy tez naglowki IP
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# w systemach windows trzeba wlaczyc wywolanie IOCTL
# przlacza w tryb nieogranicziny
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print(sniffer.recvfrom(65565))

# wylaczamy IOCTL
if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL, socket.RVALL_ON)

