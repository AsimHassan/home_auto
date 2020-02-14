import socket
def difference (list1, list2):
   return (list(set(list1) - set(list2)))
id_up=[0,1,2,3,4,5,6,7]
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
i=0
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
	
	l=[]
	data, addr = serverSock.recvfrom(1024)
	for x in data: 
		l.append(x)
	print(i)
	i=i+1
	print(difference(id_up,l))



	


