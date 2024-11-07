from scapy.all import IP, TCP, sr1, conf

def tcp_scan(target_ip, ports):
    open_ports = []

    for port in ports:
        # Create a TCP SYN packet
        tcp = TCP(dport=port, flags='S')
        ip = IP(dst=target_ip)
        packet = ip / tcp

        # Send the packet and receive the response
        response = sr1(packet, timeout=1, verbose=0)

        # Check if the response is an SYN-ACK (indicating an open port)
        if response and response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
                open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    target_ip = "100.103.118.154"  # Change to your target IP
    ports = range(1, 1025)  # Scanning ports from 1 to 1024
    
    print("Running a TCP open ports scan...")
    open_ports = tcp_scan(target_ip, ports)
    
    print(f"Open ports on {target_ip}: {open_ports}")
