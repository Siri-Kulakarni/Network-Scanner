import socket

def detect_service(ip, port):
    """
    Attempts to detect the service running on a given port by sending an appropriate request (banner grabbing or HTTP request).
    Args:
        ip (str): The IP address of the target.
        port (int): The port number to detect the service.
    Returns:
        The name of the service if identified, otherwise 'Unknown'.
    """
    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)  # Set a timeout for the connection
        sock.connect((ip, port))
        
        # If it's port 80 (HTTP), send a simple HTTP GET request
        if port == 80:
            request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
            sock.send(request.encode())
        else:
            # For other ports, send a basic 'Hello' to try banner grabbing
            sock.send(b'Hello\r\n')

        # Receive the response from the service
        banner = sock.recv(1024).decode().strip()
        sock.close()

        # Identify the service based on the banner or port number
        if "HTTP" in banner or port == 80:
            return "HTTP"
        elif "SSH" in banner or port == 22:
            return "SSH"
        elif "FTP" in banner or port == 21:
            return "FTP"
        elif "SMTP" in banner or port == 25:
            return "SMTP"
        elif "MySQL" in banner or port == 3306:
            return "MySQL"
        else:
            return "Unknown (Banner: {})".format(banner) if banner else "Unknown"

    except (socket.timeout, ConnectionRefusedError, socket.error) as e:
                return "Unknown"

ip_address =  "142.250.190.14" 
port_number =  80
service = detect_service(ip_address, port_number)
print("Port {} is running {}".format(port_number, service))
