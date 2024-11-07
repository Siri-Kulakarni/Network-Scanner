import socket

def dns_lookup(domain):
    result = {}
    
    # Get IPv4 address
    try:
        ipv4 = socket.gethostbyname(domain)
        result['IPv4'] = ipv4
    except socket.gaierror:
        result['IPv4'] = 'Not found'
    
       
    # Get CNAME (Alias)
    try:
        alias = socket.gethostbyname_ex(domain)[1]
        if alias:
            result['CNAME'] = alias[0]
        else:
            result['CNAME'] = 'None'
    except socket.gaierror:
        result['CNAME'] = 'Not found'
    

    # Get Mail Server (MX Record)
    try:
        mail_server = socket.getaddrinfo(f"mail.{domain}", None)
        result['Mail Server'] = mail_server[0][4][0]  # Show first mail server IP
    except socket.gaierror:
        result['Mail Server'] = 'Not found'

    return result

def main():
    domain = input("Enter the domain to perform DNS lookup: ")
    result = dns_lookup(domain)
    
    # Display results
    print(f"DNS Lookup for domain: {domain}")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
