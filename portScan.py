import socket
import time
import re

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def port_scan(port):
    result = s.connect_ex((target_ip, port))
    if result == 0:
        return True
    else:
        return False

def check(ip):
    if(re.search(regex, ip)):
        return True
    else:
        print("Invalid IP Address!")
        return False
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:   
    target = input("Enter IP Address to scan: ")
    if check(target):
        break
    
target_ip = socket.gethostbyname(target)

port_start = int(input("Enter port start range(default: 0): ") or 0)
port_end = int(input("Enter port end range(default: 1024): ") or 1024)

start = time.time()

print()
print('-' * 50)
print("Ports: (might take a while if there are a lot of ports, be patient)")
pnum = 0

for port in range(port_start, port_end):
    if port_scan(port):
        print("Port {}: Open".format(port))
        pnum = pnum + 1
            
if pnum == 0:
    print("No open ports found!")

print('-' * 50)
print()
print("Complete!")

end = time.time()

t = round(end - start, 3)
print("Operation finished in {} seconds".format(t))
            
