###############
import socket
import sys
from time import *
from datetime import datetime
####################
####################
#USE==> python3 to run...#
#Bandar Al Hassn.       #
#https://t.me/arb_teak #
####################
####################
ip=input ("===> \033[0;94mENTER YOUR IP TO START: ")
t1=datetime.now()
print("Scanning Start.. %s Please Wait.. "%ip)
sleep(1)
####################
try:
    for port in range(1,6553):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(s.connect_ex((ip,port))==0):
            try:
                serv=socket.getservbyport(port)

            except socket.error:
                serv="\033[0;95mUnknown Service"
            print ("Port %s Open Service:%s "%(port,serv))
        t2=datetime.now()
        t3=t2-t1
    print ("Scanning Completed On %s"%t3)
except KeyboardInterrupt:
    print("See You Soon....!")
###############################


