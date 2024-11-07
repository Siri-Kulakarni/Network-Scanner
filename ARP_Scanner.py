from scapy.all import ARP, Ether, srp, conf

def arp_scan(target_ip):
    # Create ARP request
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    # Send the packet and receive the response
    result = srp(packet, timeout=2, verbose=0)[0]

    # Parse the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    target_ip = "192.168.148.85"  # Change to your target network
    devices = arp_scan(target_ip)
    print("Running an ARP scan...")
    print("Available devices in the network:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")
