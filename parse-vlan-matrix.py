#!/usr/bin/env python3.5m


import telnetlib
import time
import getpass
import sys
import more_itertools

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
    else:
        pass

#print(v1)

for port in v1:
    print(port)

for port in v999:
    print(port)


command = sys.argv[1].encode('ascii')
user = input('Username: ').encode('ascii')
password = getpass.getpass().encode('ascii')
#enable_pass = getpass.getpass(prompt='Enter enable password: ').encode('ascii')

devices_ip = ['10.0.100.47', '10.0.100.48', '10.0.100.49']

str_ports =''

for ip in devices_ip:
        print('Connection to device {}'.format(ip))
        t = telnetlib.Telnet(ip)
        t.read_until(b':')
        t.write(user + b'\n')
        t.read_until(b':')
        t.write(password + b'\n')
#       t.write(b'enable\n')
#       t.read_until(b'Password:')
#       t.write(enable_pass + b'\n')
#       t.write(b'terminal length 0\n')
        t.write(command + b'\n')
        time.sleep(1)
#        output = t.read_very_eager().decode('ascii')
#        output = t.read_until(b'MAC').decode('ascii')
        version = t.read_until(b'Switch').decode('ascii')
#        print(output)
        device = version.split()
        print(version)
        print(device)
        t.write(b'logout\n')

# determining trunk ports
        for word in device:
                if word == 'DES-3028':
                        print('trunk ports are 25-28')
                        for port in v1:
                            if port > 24:
                                pass
                            else:
#                                str_ports = str_ports + str(port) + ','
                                print('generating config for DES-3028 and vlan 1')
                                to_range = ["{}-{}".format(groups[0],groups[-1]) for groups in map(list,more_itertools.consecutive_groups(v1))]
                                print(to_range)
#                                print(str_ports)
                        for port in v999:
                            if port > 24:
                                pass
                            else:
                                print('generating config for DES-3028 and vlan 999')
                elif word == 'DES-3550':
                        print('trunk ports are 49-50')
                        for port in v1:
                            if port > 48:
                                pass
                            else:
                                to_range = ["{}-{}".format(groups[0], groups[-1]) for groups in map(list, more_itertools.consecutive_groups(v1))]
                                print(to_range)
                        for port in v999:
                            if port > 48:
                                pass
                            else:
                                print('generating config for DES-3550 and vlan 999')
                elif word == 'DES-1228/ME':
                        print('trunk ports are 25-28')
                        for port in v1:
                            if port > 24:
                                pass
                            else:
                                print('generating config for DES-3028 and vlan 1')
                        for port in v999:
                            if port > 24:
                                pass
                            else:
                                print('generating config for DES-3028 and vlan 999')
                elif word == 'DES-3052':
                        print('trunk ports are 49-52')
                        for port in v1:
                            if port > 48:
                                pass
                            else:
                                print('generating config for DES-3550 and vlan 1')
                        for port in v999:
                            if port > 48:
                                pass
                            else:
                                print('generating config for DES-3550 and vlan 999')
                elif word == 'DES-3200-10':
                        print('trunk ports are 9-10')
                elif word == 'DES-3200-28':
                        print('trunk ports are 25-28')
                elif word == 'DES-3200-52':
                        print('trunk ports are 49-52')
                elif word == 'DES-3526':
                        print('trunk ports are 25-26')
                elif word == 'DES-3552':
                        print('trunk ports are 49-52')
                elif word == 'DGS-1210-28/ME':
                        print('trunk ports are 25-28')
#                elif word == 'DGS-1210-28/ME':
#                       print('trunk ports are 25-28')