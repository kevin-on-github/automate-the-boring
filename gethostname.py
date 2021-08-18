import socket
import subprocess

hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
print ('Hostname: ' + hostname)
print ('IP address: ' + hostip)

def getremotemachine(hostname):
    print ('Enter hostname to resolve')
    hostname = input()
    print ('Hostname: ' + hostname)
    print ('This is it ' + socket.gethostbyname(hostname))
    
getremotemachine(hostname)
