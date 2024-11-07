from scapy.all import IP, ICMP, sr1

def icmp(ip):
    packet = IP(dst=ip) / ICMP()
    reply = sr1(packet, timeout=2)
    if reply:
        return True
    return False

if __name__ == '__main__':
    ip = input("Enter target IP: ")
    if icmp(ip):
        print(f"{ip} is reachable via ICMP.")
    else:
        print(f"{ip} is not reachable.")
