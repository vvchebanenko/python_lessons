import glob
import os
import re

# files = glob.glob("*.py")
# print(files)


# for fname in files:
#     with open(fname) as f:
#         for l in f:
#             print("File: ", fname, "  lengths: ", len(l))

# print(os.listdir())


for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.log'):
            #print(os.path.join(root, file))
            with open(os.path.join(root, file)) as f:
                for l in f:
                    # print(l)
                    if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", l ):
                        print(l, end="")


