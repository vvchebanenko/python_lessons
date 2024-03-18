import glob
import os
import re

# files = glob.glob("*.log")
# print(files)


# for fname in files:
#     with open(fname) as f:
#         for l in f:
#             print("File: ", fname, "  lengths: ", len(l))

# print(os.listdir())

print("="  * 10 )
list_ip = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.log'):
            #print(os.path.join(root, file))
            with open(os.path.join(root, file)) as f:
                for l in f:
                    # print(l)
                    # if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", l ):
                    #     print(l, end="")
                    if l.find('ip address') > 0:
                        l = l.replace("ip address", "").strip().rstrip()
                        # check = lambda s: not all('0'<=x<='9' or ' ' for x in s.lower())
                        check = lambda s: not all('a'<=x<='z' or 'а'<=x<='я' for x in s.lower())
                        if check(l.replace("ip address", "").strip().rstrip()):
                            list_ip.append(l.replace("ip address", "").strip().rstrip())

list_ip_no_d = list(set(list_ip))


for ip_mask in list_ip_no_d:
    temp = ip_mask.split()
    print(f"{temp[0]}/{temp[1]}")
