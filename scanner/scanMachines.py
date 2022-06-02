import socket
import pyfiglet

ascii_banner = pyfiglet.figlet_format("IP SCANNER") 
print(ascii_banner) 
target = input("Please an IP adress: ")
splitIP = target.split('.')
dot = '.'

combIP = splitIP[0] + dot + splitIP[1] + dot + splitIP[2] + dot

firstIP = int(input("Please enter the starting number: "))
lasIp = int(input("Please enter the last number: "))

def check(addr):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((addr,135))
    if result == 0:
        return 1
    else :
        return 0

def go():
    for ip in range(firstIP,lasIp):
        addr = combIP + str(ip)
        if (check(addr)):
            print (addr, "is Up")
go()
