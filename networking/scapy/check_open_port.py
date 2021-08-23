from scapy.all import *

import sys

def tcp_scan(ip, dport):
    ans, _ = sr(IP(dst=ip)/TCP(dport=dport, sport=666, flags="S"))
    for _, returned  in ans:
        if "SA" in str(returned[TCP].flags):
            return f"for device ip {ip} port {dport} is open"
        else:
            return f"for device ip {ip} port {dport} is CLOSED"
    

def main():
    ip = sys.argv[1]
    dport = int(sys.argv[2])
    output = tcp_scan(ip, dport)
    print(output)


if __name__ == "__main__":
    main()