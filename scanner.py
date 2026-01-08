import socket

def port_scan(target_ip):
    # Common ports to scan (SSH, HTTP, HTTPS, RDP)
    ports = [21, 22, 80, 443, 3389]
    print(f"Scanning Target: {target_ip}")
    
    for port in ports:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Wait 1 second for a response
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
        s.close()

# You can test this on your own home router or 'localhost'
target = "127.0.0.1" 
port_scan(target)
