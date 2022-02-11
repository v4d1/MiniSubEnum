import socket, sys, numpy as np
from concurrent.futures import ThreadPoolExecutor
def checkDomain(subdomains):
	for subdomain in subdomains:
		try:
			print("Subdomain found: " + subdomain.strip() +"."+sys.argv[1] + " at " + socket.gethostbyname(subdomain.strip() +"."+ sys.argv[1]))
		except: pass
if __name__ == "__main__":
	splited_list = np.array_split(open(sys.argv[2], 'r').readlines(), int(sys.argv[3]))
	[ThreadPoolExecutor(max_workers=int(sys.argv[3])).submit(checkDomain, splited_list[i]) for i in range(int(sys.argv[3]))]