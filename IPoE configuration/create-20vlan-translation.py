#!/usr/bin/python3.5m

import argparse

text = "Vlan translation for DGS3627G"
parser = argparse.ArgumentParser(description = text)

parser.add_argument("--port", "-p", help="port", required=True, nargs='*')
parser.add_argument("--vlan", "-v", help="svlan", required=True)
args = parser.parse_args()

args_dict = vars(args)

port = args_dict["port"]
svlan = args_dict["vlan"]
vlan = 4090

# create vlan_translation ports 1 cvid 4090 add svid 3434

while vlan >= 4070:
    print("create vlan_translation ports " + str(port[0]) + " cvid " + str(vlan) + " add svid " + str(svlan))
    vlan -= 1
