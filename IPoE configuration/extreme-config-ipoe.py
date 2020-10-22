#!/usr/bin/python3.5m

import argparse

text = "ExtremeXOS configuration tool"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
parser.add_argument("--port", "-p", help="port to aggregation", required=True, nargs='*')
parser.add_argument("--xconn", "-x", help="primary xconnect destination", required=True, nargs='*')
args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
port = args_dict["port"]
bras = args_dict["xconn"]

## Create extreme config

## VLANS

i = int(vlan[0])
p = int(port[0])
bras = bras[0]

if bras == "10.0.96.22":
    pass
elif bras == "213.248.0.27":
    pass
else:
    print("We dont have bras", bras)
    exit()

while i <= int(vlan[1]):
    ### VLANS
    print("create vlan IPOE" + str(i))
    print("configure vlan IPOE" + str(i), "tag", str(i))
    print("configure vlan IPOE" + str(i), "add ports", str(p), "tagged")
    print("disable igmp snooping vlan IPOE" + str(i))
    ### VPLS
    print("create l2vpn vpls vpls-" + str(i), "fec-id-type pseudo-wire" , str(i))
    print("configure l2vpn vpls vpls-" + str(i), "add service vlan IPOE" + str(i))
    print("configure l2vpn vpls vpls-" + str(i), "mtu 1600")
#    print("configure l2vpn vpls vpls-" + str(i), "dot1q tag exclude")
    if bras == "10.0.96.22":
        print("configure l2vpn vpls vpls-" + str(i), "add peer 10.0.96.22 core primary")
        print("configure l2vpn vpls vpls-" + str(i), "add peer 213.248.0.27 core secondary")
    elif bras == "213.248.0.27":
        print("configure l2vpn vpls vpls-" + str(i), "add peer 213.248.0.27 core primary")
        print("configure l2vpn vpls vpls-" + str(i), "add peer 10.0.96.22 core secondary")
    else:
        print("We dont have bras", bras)
    i += 1



