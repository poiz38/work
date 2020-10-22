#!/usr/bin/python3.5m

import telnetlib
import time
import getpass
import sys
import string
import more_itertools
import argparse

comma=','

text = "Vlan creator for access d-links, usage: -v vlan-id(multiply vlan supported, separate with space, where first vlan is a vlan on this switch), -p last port"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
#parser.add_argument("--port", "-p", help="last port on dlink", required=True)

args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
#port = int(args_dict["port"])


#заполняем словарь d из файла
d = {}
with open("vlan-matrix") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value


#заполняем словарь n данными из словаря d, убирая всё, кроме нулевого параметра листа внутри ключа словаря
n = {}

for key in d:
#    print(key, d[key])
    n[key] = d[key][0]
#    print(d[key][0])
#print(n)


v1 = []
v999 = []
v1000 = []
for key in n:
    if int(key) == 1:
#        print('vlan ' + key + ' ports ' + n[key])
        str_v1 = n[key].split(',')
#        print(str)
        v1 = list(map(int,str_v1))
#        print(v1)
    elif int(key) == 999:
        str_v999 = n[key].split(',')
#        print('vlan ' + key + ' ports ' + n[key])
        v999 = list(map(int,str_v999))
    elif int(key) == 1000:
        str_v1000 = n[key].split(',')
        #        print('vlan ' + key + ' ports ' + n[key])
        v1000 = list(map(int, str_v1000))
    else:
        pass
#print(v1)


for trunk_port in v1000:
#    print(trunk_port)
    v1.remove(trunk_port)
    v999.remove(trunk_port)

#for port in v1:
#    print(port)

#for port in v999:
#   print(port)

range_v1 = ["{}-{}".format(groups[0],groups[-1]) for groups in map(list,more_itertools.consecutive_groups(v1))]
range_v999 = ["{}-{}".format(groups[0],groups[-1]) for groups in map(list,more_itertools.consecutive_groups(v999))]
range_v1000 = ["{}-{}".format(groups[0],groups[-1]) for groups in map(list,more_itertools.consecutive_groups(v1000))]
range_access_ports = range_v1 + range_v999
#print(range_access_ports)

#print(range_v1)
#print(range_v999)
#print(range_v1000)

print("")
print("#Config for access D-link for preparation:")
print("")


for trunk_port in range_v1000:
    for i in vlan:
        print("create vlan v" + i,  "tag", i)
        print("config vlan v" + i, "add tagged "+ str(trunk_port))

# все клиентские порты
access_port_result = comma.join(range_access_ports)
#print(access_port_result)

print("enable dhcp_local_relay")
print("config dhcp_local_relay vlan vlanid " + vlan[0], "state enable")
print("config dhcp_local_relay option_82 remote_id default")
print("config dhcp_local_relay option_82 ports " + access_port_result + " policy replace")

# Config for access D-link for planned works

print("")
print("#Config for access D-link for planned works:")
print("")

# делаем результирующую строку портов во влане 1
v1_port_result = comma.join(range_v1)
# делаем результирующую строку портов во влане 999
v999_port_result = comma.join(range_v999)

print("config vlan vlanid 1 delete " +  str(v1_port_result))

#проверяем что в 999 влане есть порты
if v999_port_result:
    print("config vlan vlanid 999 delete " +  str(v999_port_result))
else:
    pass

print("config vlan vlanid " + vlan[0], "add untagged " + access_port_result + " advertisement disable")

#if port > 48:
#	print("config vlan vlanid 1 delete 1-48")
#	print("config vlan v" + vlan[0], "add untagged 1-48 advertisement disable")
#else:
#	print("config vlan vlanid 1 delete 1-24")
#	print("config vlan v" + vlan[0], "add untagged 1-24 advertisement disable")