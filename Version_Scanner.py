import socket

def scan_version(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target_host, target_port))
        banner = sock.recv(1024)
        print(f"Version information for {target_host}:{target_port}: {banner.decode().strip()}")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    target_host = input("Enter the target host IP address: ")
    target_port = int(input("Enter the target port: "))
    
    scan_version(target_host, target_port)