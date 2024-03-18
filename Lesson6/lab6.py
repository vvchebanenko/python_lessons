import glob
import os
import re
import ipaddress

print("="  * 10 )
list_ip = []


def reg_func(string:str = "") -> object:

    m = re.search(r"(ip address){1} (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}){1} (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}){1}", string)
    if m:
        # print(str(m.group(2)) + "/" + str(m.group(3)))
        return ipaddress.IPv4Interface((m.group(2)) + "/" + str(m.group(3)))
    else:
        pass

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.log'):
            #print(os.path.join(root, file))
            with open(os.path.join(root, file)) as f:
                for l in f:
                    res = reg_func(l)
                    if res:
                        print(res.ip, res.netmask)

