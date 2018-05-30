from scapy.all import *

def getIP(domain):
    answer = sr1(IP(dst = "8.8.8.8")/UDP()/DNS(rd = 1,qd = DNSQR(qname = domain)),timeout = 1)  

    if(answer[DNS].rcode != 0):
        print("Khong tim thay dia chi IP")
        return
    if(answer[DNS].an.type != 1):
        print("Khong tim thay dia chi IPv4")
        return
    #answer.show()
    for i in range (0,answer[DNS].ancount):
        print("IP = " +str(answer[DNS].an[i].rdata))

def getDomain(ip):
    # chuyen dia chi IP thanh ten mien nguoc
    ip = ip.split('.')                            
    ip.reverse()                                    
    ip = '.'.join(ip) + ".in-addr.arpa"
    answer = sr1(IP(dst= "8.8.8.8")/UDP()/DNS(rd = 1, qd = DNSQR(qname = ip , qtype='PTR')),timeout = 1)
    if(answer[DNS].rcode != 0 ):
        print("Khong tim thay ten mien")
        return 
    if(answer[DNS].an.type != 12 ):
        print("Khong tim thay ten mien")
        return 
    #answer.show()
    for i in range (0,answer[DNS].ancount):
        print("domain = " + str(answer[DNS].an[i].rdata[:-1]))   

choice = 0
while(choice != 3):
    print('Nhap vao lua chon cua ban:')
    print('1: Phan giai ten mien thanh dia chi IP')
    print('2: Phan giai IP thanh ten mien')
    print('3: Thoat')
    choice = int(input());
    if(choice == 1):
        print('Nhap vao ten mien can phan giai:')
        domain = input();
        getIP(domain)
    if(choice == 2):
        print('Nhap vao dia chi IP can phan giai:')
        ip = input()
        getDomain(ip)
    print()