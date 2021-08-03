#!/bin/python3

import os, sys

if len(sys.argv) == 2:
	ip = sys.argv[1]

	nlports = os.popen('nmap -T4 -p- {} | grep "open" | cut -d "/" -f 1'.format(ip), 'r').readlines()

	ports = []

	for port in nlports:
		ports.append(port.strip())

	portsString = ','.join(ports)
	
	print("Ports open: {}\n".format(portsString))

	os.system('nmap -T4 -p {} -A {}'.format(portsString, ip))

else:
	print("Enter the IP address as an argument")
	print("Syntax: ./scan.py 127.0.0.1")
