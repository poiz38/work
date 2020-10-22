#!/usr/bin/env python3

d = {}
with open("vlans-dhcp-relay.txt") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value
for key in d:
	name = d[key]

	print("enable bootprelay vlan {0}".format(name[0]))
	print("configure bootprelay vlan {0} add 10.26.2.10".format(name[0]))
