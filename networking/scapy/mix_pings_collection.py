from scapy.all import *

def ping_icmp(ip):
    ans, unauns = sr(IP(dst=ip)/ICMP())
    return ans

def ping_tcp(ip, dport):
    ans, uans = sr(IP(dst=ip)/TCP(sport=8000, dport=dport, flags="S"))
    return ans

def ping_udp(ip):
    ans, uans = sr(IP(dst=ip)/UDP(sport=8000, dport=0))
    return ans

def summary_ping(ans):
    for sending, returned in ans:
        print(f"{returned[IP].src} is alive")

def main():
    print("*** ICMP PINGING ****\n")
    ans = ping_icmp("172.26.1.1")
    print("*** TCP PINGING ****\n")
    ans = ping_tcp("172.26.1.1", 22)
    print("*** UDP PINGING ****\n")
    ans = ping_udp("172.26.1.1")
    summary_ping(ans)
    

if __name__ == "__main__":
    main()