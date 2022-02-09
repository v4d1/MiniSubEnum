#!/usr/bin/env python
#Usage python3 MiniSubEnum_threads.py domain wordlist.txt num_threads --> example: python3 MiniSubEnum_threads.py facebook.com subdomains-5000.txt 20
import socket, sys, numpy as np
from concurrent.futures import ThreadPoolExecutor
def checkDomain(subdomains):
	for subdomain in subdomains:
		try:
			socket.gethostbyname(subdomain.strip() +"."+ sys.argv[1])
			print("Subdomain found: " + subdomain.strip() +"."+sys.argv[1])
		except: pass
if __name__ == "__main__":
	wordlist = open(sys.argv[2], 'r')
	splited_list = np.array_split(wordlist.readlines(), int(sys.argv[3]))
	executor = ThreadPoolExecutor(max_workers=int(sys.argv[3]))
	[executor.submit(checkDomain, splited_list[i]) for i in range(int(sys.argv[3]))]