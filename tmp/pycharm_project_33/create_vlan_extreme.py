#!/usr/bin/env python3

d = {}
with open("vlans.txt") as file:
    for line in file:
        key, *value = line.split()
        d[key] = value
for key in d:
	name = d[key]
#to delete vlan uncomment below
#	print("delete vlan {0}".format(name[0]))
#to create vlan uncomment below
#	print("create vlan {0}".format(name[0]))
#	print("configure vlan {0} tag {1}".format(name[0],key))
#	print("configure vlan {0} add ports {1} tagged".format(name[0],name[1]))
#to create l3 vlan uncomment below
#	try:
#		print("configure vlan {0} ipaddress {2} {3}".format(name[0],name[1],name[2],name[3]))
#		print("enable ipforwarding vlan {0}".format(name[0]))
#	except IndexError:
#	print("# vlan {0} doesn't have ipaddress".format(name[0]))
#		pass
#to create stp rapid-pvst uncomment below
#	print("create stpd {0}".format(name[0]))
#	print("configure stpd {0} mode dot1w".format(name[0]))
#	print("configure stpd {0} add vlan {0} ports {1} pvst-plus".format(name[0],name[1]))
#	print("configure stpd {0} tag {1}".format(name[0],key))
#	print("enable stpd {0}".format(name[0]))

#to shutdown L3 Vlan on cisco uncomment below
#	try:
#		if name[2]:
#			print("int vlan{0}".format(key))
#			print("shutdown")
#		else:
#			pass
#	except IndexError:
#		pass
#	print("enable bootprelay vlan {0}".format(name[0]))
#	print("configure bootprelay vlan {0} add 10.26.2.10".format(name[0]))
#to get vlan list uncomment below
#	print(key)
#disable ipv4
	print("disable ipforwarding vlan {0}".format(name[0]))
	print("unconfigure vlan {0} ipaddress".format(name[0]))
	print("int vlan{0}".format(key))
	print("no shut")
