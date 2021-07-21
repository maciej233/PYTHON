from scapy.all import *
import sys

def tcp_scan(IP, dport):
    #ans, uans = 
    pass



def main():
    destination = sys.argv[1]
    dport = int(sys.argv[2])
    scan_result = tcp_scan(destination, dport)
    print(scan_result)

if __name__ == "__main__":
    main()