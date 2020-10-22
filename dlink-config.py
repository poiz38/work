#!/usr/bin/env python3

import telnetlib
import time
import getpass
import sys


command = sys.argv[1].encode('ascii')
user = input('Username: ').encode('ascii')
password = getpass.getpass().encode('ascii')
#enable_pass = getpass.getpass(prompt='Enter enable password: ').encode('ascii')

devices_ip = ['10.0.100.47', '10.0.100.48', '10.0.100.49']

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
                elif word == 'DES-3550':
                        print('trunk ports are 49-50')
                elif word == 'DES-1228/ME':
                        print('trunk ports are 25-28')
                elif word == 'DES-3052':
                        print('trunk ports are 49-52')
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