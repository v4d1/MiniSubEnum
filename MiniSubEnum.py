import socket, sys
for line in open(sys.argv[2], 'r').readlines():
	try:
		print(line.strip() +"." + sys.argv[1] + " at " + socket.gethostbyname(line.strip() +"." + sys.argv[1]))
	except: pass