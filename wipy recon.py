import platform, subprocess
import socket

# For getting MAC from IP
from getmac import get_mac_address



# Pings the provided IP
def ping(host_or_ip, packets=1, timeout=1000):
    if platform.system().lower() == 'windows':
        command = ['ping', '-n', str(packets), '-w', str(timeout), host_or_ip]
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, creationflags=0x08000000)
        return result.returncode == 0 and b'TTL=' in result.stdout
    else:
        command = ['ping', '-c', str(packets), '-w', str(timeout), host_or_ip]
        result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode == 0


def main():
    # Title Styling
    print("-" * 60)
    print(" " * 23 + "WIPY RECON")
    print("-" * 60)
    print()
    
    
    # Gets the first three parts of local IP
    self_ip = socket.gethostbyname(socket.gethostname())
    ip = self_ip.split(".")
    ip = ip[:-1]
    gen_ip = ip[0] + "." + ip[1] + "." + ip[2] + "."


    # Takes Input for operation to perform
    inp = input("""[0] Number of devices connected
[1] MAC Addresses of devices connected
[2] IP Addresses of devices connected\n\n>>> """)
    print()


    if inp == "1":
        print("The MAC addresses of the devices connected to this network are:")
    elif inp == "2":
        print("The IP addresses of the devices connected to this network are:")
    
    
    # Loops over the IP with the fourth part being iterated
    length = []
    for i in range(256):
        addr = gen_ip + str(i)
        if ping(addr):
            mac = get_mac_address(ip = addr)
            if inp == "1":
                print(mac)
            elif inp == "2":
                if mac != None:
                    print(addr)
            if mac != None:        
                length.append(" ")
            
    if inp == "0":
        print("The number of devices connected are " + str(len(length)))


if __name__ == "__main__":
    main()
