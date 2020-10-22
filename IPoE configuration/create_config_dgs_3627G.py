#!/usr/bin/python3.5m

import argparse

text = "vlan configuration tool for Dlink 3630"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
parser.add_argument("--lastport", "-lp", help="last port", required=True, nargs="*")
parser.add_argument("--trunkport", "-tp", help="trunk port", required=True, nargs="*")
args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
lastport = args_dict["lastport"]
trunkport = args_dict["trunkport"]

## Create vlan config

# create vlan v3278 tag 3278
# config vlan v3278 add tagged 5,20
# config vlan v3278 add untagged 22

i = int(vlan[1])
p = 1
lp = int(lastport[0])
tp = int(trunkport[0])

while i >= int(vlan[0]) and p <= lp:
    print("create vlan v" + str(i) + " tag " + str(i))
    print("config vlan v" + str(i) + " add tagged " + str(tp))
    print("config vlan v" + str(i) + " add untagged " + str(p))
    i -= 1
    p += 1

k = int(vlan[0])

#while k <= int(vlan[1]):
#    print("service encapsulation svid " + str(k))
#    print(" xconnect vfi " + str(k))
#    print(" exit")
#    k += 1
