import socket
import pyfiglet
import sys
from datetime import datetime
banner=pyfiglet.figlet_format("**  itado3i  **\n\t  port scanner ")
print(banner)
file=open("portscanner.txt","w")
try:
    host=socket.gethostbyname(input("enter host : "))  #finding ip of the target(input if it is (dns) else if it is (ip) it simple return ip)
    print("ip address of the host : {}\n".format(host)) 
    file.write("ip address of the host : {}\n".format(host))

    start_time=datetime.now()
    for port in range(1,1025): #finding all open ports from 1 to 1025

        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating tcp ipv4 endpoint
        sock.settimeout(0.001)
        result=sock.connect_ex((host, port))
        try:
            if result==0:
                print("port no : {} opened protocol service name :{}".format(port,socket.getservbyport(port,"tcp")))
                file.write("port no : {} opened protocol service name :{}\n".format(port,socket.getservbyport(port,"tcp")))
        except socket.error :
                print("port no : {} opened protocol service name :{}".format(port,"unknown"))
                file.write("port no : {} opened protocol service name :{}\n".format(port,"unknown"))



    end_time=datetime.now()
    print("\nscan time :{}".format(end_time-start_time))
    file.write("\nscan time :{}".format(end_time-start_time))
except socket.gaierror:
    print("hostname name might be wrong")
    sys.exit()
except socket.error:
    print("cant reach the server")
    sys.exit()
