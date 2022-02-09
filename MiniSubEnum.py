#!/usr/bin/env python
#Usage python3 MiniSubEnum.py domain wordlist.txt --> example: python3 MiniSubEnum_threads.py facebook.com subdomains-5000.txt
import socket, sys
wordlist = open(sys.argv[2], 'r')
entries = wordlist.readlines()
for entry in entries:
	try:
		socket.gethostbyname(entry.strip() +"."+ sys.argv[1])
		print("Subdomain found: " + entry.strip() +"."+ sys.argv[1])
	except: pass