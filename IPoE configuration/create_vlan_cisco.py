#!/usr/bin/python3.5m

import telnetlib
import time
import getpass
import sys
import string
import more_itertools
import argparse

comma=','

text = "Vlan creator for cisco CORE, usage: -v starting vlan ending vlan"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]

i = int(vlan[0])

while i <= int(vlan[1]):
    print('vlan', i)
    print("name ipoe" + str(i))
    i += 1