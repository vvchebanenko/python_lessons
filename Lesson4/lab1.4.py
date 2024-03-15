import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network, ipaddress.IPv4Address):
    f_subnet = []
    def __init__(self):
        f_subnet = []
        for i in range(0,51):
            net = random.randint(0x0b00000, 0xdfd00000)# 11.0.0.0 - 223.0.0.0
            #print("net")
            #print(net)
            mask = random.choice(["/8", "/24"])
            #print("mask")
            #print(mask)
            net_mask = str(ipaddress.IPv4Address(net)) + mask
            #print("ipaddress.IPv4Address(net) + mask")
            #print(str(ipaddress.IPv4Address(net)) + mask)
            subnet = ipaddress.ip_network(ipaddress.IPv4Network(str(ipaddress.IPv4Address(net)) + mask, strict=False))
            #print(subnet)
            f_subnet.append(subnet)

        for _ in f_subnet:
            print(_)

    def fake_subnet(self):
        print()



net1 = IPv4RandomNetwork()
# print(net1.subnets(4,6))
# for i in net1.subnets(4,6):
#     print()
# print()
# print(net1.is_link_local)
# print(net1.network_address)

#
# for _ in net1:
#     print(_)