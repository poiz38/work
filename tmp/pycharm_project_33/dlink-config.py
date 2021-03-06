#!/usr/bin/env python3

import telnetlib
import time
import getpass
import sys


command = sys.argv[1].encode('ascii')
user = input('Username: ').encode('ascii')
password = getpass.getpass().encode('ascii')
#enable_pass = getpass.getpass(prompt='Enter enable password: ').encode('ascii')

devices_ip = ['10.0.100.47']

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
        output = t.read_very_eager().decode('ascii')
        print(output)
        t.write(b'logout\n')
