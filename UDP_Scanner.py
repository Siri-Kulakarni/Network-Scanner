from scapy.all import IP, UDP, ICMP, sr1

def udp_scan(target_ip, ports):
    open_ports = []

    for port in ports:
        # Create a UDP packet
        udp = UDP(dport=port)
        ip = IP(dst=target_ip)
        packet = ip / udp

        # Send the packet and receive the response
        response = sr1(packet, timeout=1, verbose=0)

        # Check if there's no response, which might indicate the port is open or filtered
        if response is None:
            open_ports.append(port)
        else:
            # Check if the response has an ICMP layer
            if response.haslayer(ICMP):
                # Check if the ICMP type indicates that the port is unreachable
                if response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code == 3:
                    continue  # Port is closed (destination unreachable)

    return open_ports

if __name__ == "__main__":
    target_ip = "<ip-address>"  # Change to your target IP
    ports = range(1, 1025)  # Scanning ports from 1 to 1024

    print("Running a UDP port scan...")
    open_ports = udp_scan(target_ip, ports)
    
    print(f"Open UDP ports on {target_ip}: {open_ports}")
