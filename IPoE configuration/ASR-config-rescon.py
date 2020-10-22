#!/usr/bin/python3.5m

import argparse

text = "ASR configuration tool"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]

## Create dhcp config

print("dhcp ipv4")
i = int(vlan[0])

while i <= int(vlan[1]):
    print("interface Bundle-Ether1." + str(i) + " proxy profile RESCON")
    i += 1


## Create interface config

k = int(vlan[0])

while k <= int(vlan[1]):
    print("interface bundle-ether 1." + str(k))
    print(" description HOMENET VLAN " + str(k))
    print(" mtu 1600")
    print(" ipv4 point-to-point")
    print(" ipv4 unnumbered Loopback2")
    print(" arp learning disable")
    print(" service-policy type control subscriber IPOE-POLICYMAP-RESCON")
    print(" ipsubscriber ipv4 l2-connected")
    print("  initiator dhcp")
    print(" !")
    print("exit")
    print("encapsulation ambiguous dot1q " + str(k) + " second-dot1q 2000-4094")
    k += 1