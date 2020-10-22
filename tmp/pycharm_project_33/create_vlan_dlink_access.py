#!/usr/bin/env python3
import argparse

text = "Vlan creator for access d-links, usage: -v vlan-id(multiply vlan supported, separate with space, where first vlan is a vlan on this switch), -p last port"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--vlan", "-v", help="vlans", required=True, nargs='*')
parser.add_argument("--port", "-p", help="last port on dlink", required=True)

args = parser.parse_args()

args_dict = vars(args)

vlan = args_dict["vlan"]
port = int(args_dict["port"])


# Config for access D-link for preparation

print("")
print("#Config for access D-link for preparation:")
print("")

for i in vlan:
	print("create vlan v" + i,  "tag", i)
	if port > 50:
		print("config vlan v" + i, "add tagged 49-52")
	elif port > 48:
		print("config vlan v" + i, "add tagged 49-50")
	else:
		print("config vlan v" + i, "add tagged 25-26")

if port > 48:
	print("enable dhcp_local_relay")
	print("config dhcp_local_relay vlan vlanid " + vlan[0], "state enable")
	print("config dhcp_local_relay option_82 remote_id default")
	print("config dhcp_local_relay option_82 ports 1-48 policy replace")
else:
	print("enable dhcp_local_relay")
	print("config dhcp_local_relay vlan vlanid " + vlan[0], "state enable")
	print("config dhcp_local_relay option_82 remote_id default")
	print("config dhcp_local_relay option_82 ports 1-24 policy replace")

# Config for access D-link for planned works

print("")
print("#Config for access D-link for planned works:")
print("")

if port > 48:
	print("config vlan vlanid 1 delete 1-48")
	print("config vlan v" + vlan[0], "add untagged 1-48 advertisement disable")
else:
	print("enable dhcp_local_relay")
	print("config vlan v" + vlan[0], "add untagged 1-24 advertisement disable")
