from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
    target = input('enter the IP to be scanned: ')
    ta_IP = gethostbyname(target)
    print('Starting scan on IP', ta_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        
        conn = s.connect_ex((ta_IP, i))
        if(conn == 0) :
            print ('Port %d: OPEN' % (i,))
            s.close()
print('Time spent:', time.time() - startTime)
