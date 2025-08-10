import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    sock.settimeout(1)  # Timeout after 1 second if no response
    result = sock.connect_ex((ip, port))  # Try to connect to the IP and port
    sock.close()  # Close the socket
    return result == 0  # If result is 0, connection succeeded (port open)

if __name__ == "__main__":
    target_ip = input("Enter IP address to scan: ")  # Ask user for IP to scan
    for port in range(1, 1025):  # Check ports from 1 to 1024
        if scan_port(target_ip, port):
            print(f"Port {port} is open")
