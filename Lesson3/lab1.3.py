from pysnmp.hlapi import *

engine = SnmpEngine()
comm_data = CommunityData("public", mpModel=0)
transport = UdpTransportTarget(("10.31.70.209", 161))
context_data = ContextData()

snmp_version = ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)
snmp_interfaces = ObjectIdentity("1.3.6.1.2.1.2.2.1.2")

result = getCmd(engine, comm_data, transport, context_data, ObjectType(snmp_version))

def print_res(x):
    for _ in x:
        print(x)

print(type(result))
print("========================")
print("result is:")
# for x in result:
#     for y in x:
#         print(type(y))
#         print(y)
for _ in result:
    print_res(_)

print("\n"*5)
result = getCmd(engine, comm_data, transport, context_data, ObjectType(snmp_version))
print("result 2 is:")
for r in result:
    for r2 in r[3]:
        print(r2)
#
# print("result 2 is:")
# for r in result:
#     for r2 in r[3]:
#         print(r2)