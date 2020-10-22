#!/usr/bin/python3.5m

import argparse

text = "Xconnect configuration tool for Dlink 3630"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
parser.add_argument("--target", "-t", help="remote host", required=True)
args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
host = args_dict["target"]


## Create xconnect config

i = int(vlan[0])

while i <= int(vlan[1]):
    print("l2 vfi " + str(i) + " manual")
    print(" vpn id " + str(i))
    print(" mtu 1600")
    print(" vlanmode changevlan " + str(i))
    print(" neighbor remote " + host + " encapsulation mpls")
    i += 1

k = int(vlan[0])

while k <= int(vlan[1]):
    print("service encapsulation svid " + str(k))
    print(" xconnect vfi " + str(k))
    print(" exit")
    k += 1


