# Identify IP Address and Subnet Details

import ipaddress

ip = input("Enter IP address: ")
mask = input("Enter subnet mask: ")

# Create network
network = ipaddress.IPv4Network(ip + "/" + mask, strict=False)

print("\nIP Address:", ip)
print("Subnet Mask:", network.netmask)
print("Network Address:", network.network_address)
print("Broadcast Address:", network.broadcast_address)

# Find first and last usable IP
hosts = list(network.hosts())

if len(hosts) > 0:
    print("First Address:", hosts[0])
    print("Last Address:", hosts[-1])
else:
    print("No usable host addresses")

# Display MAC address
print("\nTo find MAC Address, use the command: ipconfig /all")