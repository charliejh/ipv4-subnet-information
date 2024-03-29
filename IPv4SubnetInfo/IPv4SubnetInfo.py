"""
IPv4 Subnet Information v2.0
By Charlie Harris

[1] Example input: 192.168.0.1
                   202.144.10.40

[2] Example input: 192.168.1.25/24
                   10.10.10.10 255.255.0.0

[3] Example input: 192.168.0.0 500
"""

from netaddr import *

def getInformation(ip):

    if not ip:
        ip = input("\nEnter IP address and subnet mask/CIDR notation: ")
    if " " in ip:
        ip = ip.split(" ")
    elif "/" in ip:
        ip = ip.split("/")
    elif ip == "":
        return

    if '.' in ip[1]:
        ip.append(str(IPAddress(ip[1]).netmask_bits()))
    else:
        ip.insert(1, str(IPNetwork(ip[0] + "/" + ip[1]).netmask))
    ip.append(str(IPNetwork(ip[0] + "/" + ip[2]).network))
    ip.append(str(IPNetwork(ip[0] + "/" + ip[2]).broadcast))
    ip.append(str(IPNetwork(ip[0] + "/" + ip[2]).size - 2))
    ip.append(ip[3][:-1] + str(int(ip[3][-1:]) + 1))
    ip.append(ip[4][:-1] + str(int(ip[4][-1:]) - 1))

    print("IP Address: " + ip[0] + "\nSubnet Mask: " + ip[1] + "\nCIDR: /" + ip[2] + "\nNetwork Address: " + ip[3] +
          "\nBroadcast Address: " + ip[4] + "\nHosts: " + ip[5] + "\nFirst IP: " + ip[6] + "\nLast IP: " + ip[7])


def reqSubnet():

    ip = input("\nEnter network IP address and the required number of hosts: ")
    ip = ip.split(" ")
    for i in range(32, 0, -1):
        if int(IPNetwork(ip[0] + "/" + str(i)).size - 2) >= int(ip[1]):
            del ip[1]
            ip.append(str(i))
            break
    getInformation(ip)


def getIPInfo():

    ip = input("\nEnter IP Address: ")
    ip = IPAddress(ip)
    print(str(ip) + " Categorisation: ")
    if ip.is_unicast() and not ip.is_private():
        print("Public")
    if ip.is_private():
        print("Private")
    if ip.is_reserved():
        print("Reserved")
    if ip.is_multicast():
        print("Multicast")
    if ip.is_unicast():
        print("Unicast")
    if ip.is_loopback():
        print("Loopback")


def main():

    while True:
        choice = input("\n"
                       "[1] Get IP Address Categorisation\n"
                       "[2] Gather Subnet Information\n"
                       "[3] Calculate Required Subnet\n"
                       "[4] Exit Program\n"
                       "Choice: ")
        if choice == "1":
            getIPInfo()
        elif choice == "2":
            ip = []
            getInformation(ip)
        elif choice == "3":
            reqSubnet()
        elif choice == "4":
            print("Quitting program...")
            break;
        else:
            print("Please enter a valid choice. Try again.")


if __name__ == '__main__':
    print("IPv4 Subnet Information\n-----------------------")
    main()
