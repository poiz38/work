#!/usr/bin/python3.5m

import argparse

text = "Xconnect configuration tool for Cisco 6500"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
parser.add_argument("--port", "-p", help="source port", required=True, nargs='*')
parser.add_argument("--target", "-t", help="remote host", required=True)
args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
source = args_dict["port"]
host = args_dict["target"]


## Create xconnect config

i = int(vlan[0])

while i <= int(vlan[1]):
    print("interface " + str(source[0]) + "." + str(i))
    print(" description INFRA ipoe" + str(i))
    print(" encapsulation dot1Q " + str(i))
    print(" xconnect " + host, str(i) + " encapsulation mpls")
    if host == "213.248.0.27":
        print("  backup peer 10.0.96.22 " + str(i))
    elif host == "10.0.96.22":
        print("  backup peer 213.248.0.27 " + str(i))
    print("  mtu 1600")
    i += 1