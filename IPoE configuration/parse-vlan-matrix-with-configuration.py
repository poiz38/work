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
parser.add_argument("--switch", "-s", help="ip addr", required=True)


args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
#port = int(args_dict["port"])
switch = args_dict["switch"]

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
    if v999:
        v999.remove(trunk_port)
    else:
        pass

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

commands_vlan = []
commands_dhcp = []

print("")
print("#Config for access D-link for preparation:")
print("")


for trunk_port in range_v1000:
    for i in vlan:
        print("create vlan v" + i,  "tag", i)
        print("config vlan v" + i, "add tagged "+ str(trunk_port))
        com1 = "create vlan v" + i + " tag " + i
        com2 = "config vlan v" + i + " add tagged " + str(trunk_port)
        commands_vlan.append(com1)
        commands_vlan.append(com2)
# все клиентские порты
access_port_result = comma.join(range_access_ports)
#print(access_port_result)

print("enable dhcp_local_relay")
print("config dhcp_local_relay vlan vlanid " + vlan[0], "state enable")
print("config dhcp_local_relay option_82 remote_id default")
print("config dhcp_local_relay option_82 ports " + access_port_result + " policy replace")

com3 = "enable dhcp_local_relay"
com4 = "config dhcp_local_relay vlan vlanid " + vlan[0] + " state enable"
com5 = "config dhcp_local_relay option_82 remote_id default"
com6 = "config dhcp_local_relay option_82 ports " + access_port_result + " policy replace"

commands_dhcp.append(com3)
commands_dhcp.append(com4)
commands_dhcp.append(com5)
commands_dhcp.append(com6)

user = input('Username: ').encode('ascii')
password = getpass.getpass().encode('ascii')
enable_pass = getpass.getpass(prompt='Enter enable password: ').encode('ascii')

command = b'show switch'
save_command = b'save'

for command in commands_vlan:
    print(command)
for command in commands_dhcp:
    print(command)

# Заливаем сгенеренный конфиг для предврительных работ на коммутатор

print('Connection to device {}'.format(switch))
t = telnetlib.Telnet(switch)
t.read_until(b':')
t.write(user + b'\n')
t.read_until(b':')
t.write(password + b'\n')
t.write(b'enable admin\n')
t.read_until(b'Password:')
t.write(enable_pass + b'\n')
for command in commands_vlan:
    t.write(command.encode('ASCII') + b'\n')
for command in commands_dhcp:
    t.write(command.encode('ASCII') + b'\n')
time.sleep(10)
t.write(save_command + b'\n')
time.sleep(5)
t.write(b'logout\n')
time.sleep(1)
output = t.read_very_eager().decode('ascii')
#        output = t.read_until(b'MAC').decode('ascii')
#        version = t.read_until(b'Switch').decode('ascii')
print(output)
#        device = version.split()
#        print(version)
#        print(device)


# Config for access D-link for planned works

print("")
print("#Config for access D-link for planned works:")
print("")
print(switch)

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