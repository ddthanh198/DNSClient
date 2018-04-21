from scapy.all import *

def getIP(domain):
    answer = sr1(IP(dst = "8.8.8.8")/UDP(dport = 53)/DNS(rd = 1,qd = DNSQR(qname = domain)),timeout = 1,verbose = 1)
    #answer.show()                          # hien thi tat ca thong tin nhan ve
    #print(answer[DNS].rcode)              # kiem tra ma cua rcode
    #print(answer[DNS].an.type)            # type = 1 la kieu dang IPv4
    if(answer[DNS].rcode != 0):
        print("Khong tim thay dia chi IP")
        return
    if(answer[DNS].an.type != 1):
        print("Khong tim thay dia chi IPv4")
        return
    return answer[DNS].an.rdata

def getDomain(ip):
    ip = ip.split('.')                             # tach dia chi IPv4 tu xxx.yyy.zzz.ttt thanh danh sach {xxx yyy zzz ttt}
    ip.reverse()                                   # dao nguoc thu tu cac phan tu trong danh sach 
    ip = '.'.join(ip) + ".in-addr.arpa"            # ttt.zzz.yyy.xxx.in-addr.arpa la cau truc ten mien nguoc
    answer = sr1(IP(dst= "8.8.8.8")/UDP(dport = 53)/DNS(rd = 1, qd = DNSQR(qname = ip , qtype='PTR')),timeout = 1, verbose = 0)
    #answer.show()
    #print(answer[DNS].rcode)
    #print(answer[DNS].an.type) 
    if(answer[DNS].rcode != 0 ):
        print("Khong tim thay ten mien")
        return 
    if(answer[DNS].an.type != 12 ):
        print("Khong tim thay ten mien")
        return 
    return answer[DNS].an.rdata[:-1]   

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
        print("IP = " + str(getIP(domain)))
    if(choice == 2):
        print('Nhap vao dia chi IP can phan giai:')
        ip = input()
        print("domain = " + str(getDomain(ip)))
    print()