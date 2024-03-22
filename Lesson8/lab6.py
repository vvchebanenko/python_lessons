import glob
import os
import re
import ipaddress

print("="  * 10 )



def reg_func(string:str = "") -> object :

    m = re.search(r"(ip address){1} (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}){1} (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}){1}", string)
    if m:
        # print(str(m.group(2)) + "/" + str(m.group(3)))
        return ipaddress.IPv4Interface((m.group(2)) + "/" + str(m.group(3)))
    else:
        pass

def get_ip() -> list :
    ip_list = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.log'):
                #print(os.path.join(root, file))
                with open(os.path.join(root, file)) as f:
                    for l in f:
                        res = reg_func(l)
                        # print(l)
                        if res:
                            # print(res.ip, res.netmask)
                            ip_list.append(str(res.ip) + " - " + str(res.netmask))
    return ip_list

# get_ip()