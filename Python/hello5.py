import socket
import uuid

def get_ip_address():
    # Get the IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    return ip_address

def get_mac_address():
    # Get the MAC address (may not work on all systems)
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return mac_address

def generate_finder_code():
    # Generate a unique Finder code (you can customize this)
    finder_code = uuid.uuid4().hex[:8].upper()
    return finder_code

if __name__ == "__main__":
    ip_address = get_ip_address()
    mac_address = get_mac_address()
    finder_code = generate_finder_code()
    
    print("IP Address:", ip_address)
    print("MAC Address:", mac_address)
    print("Finder Code:", finder_code)
