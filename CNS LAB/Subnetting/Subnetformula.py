import counter
import ipchecker
import math


def Subnetor():
    ip = ipchecker.ipchecker()
    # checks
    ipchecks = bin(int(ip.split('.')[0])).split('b')[1]
    ipcut = str(ipchecks[:3])
    if ipcut == '110':
        ipsplit = ip.split('.')
        realip = str(ipsplit[0]+'.'+ipsplit[1]+'.'+ipsplit[2]+'.')
        # for C class deafult subnet is 255.255.255.0
        deafultsubnetmask = "255.255.255.0".split('.')

        lastoct = int(ipsplit[3])
        subnets = int(input("How many subnets do we want?:"))
        # basically i need to find n of 2^n= subnets
        neededBits = int(math.log(subnets, 2))
        host = (2**(8-neededBits))-2
        print(f"Each subnet can hold {host} hosts")
        if host < 254:
            lastsub = 254-host
            deafultsubnetmask[3] = str(lastsub)
        binsubnet = []
        for i in deafultsubnetmask:
            binsubnet.append(bin(int(i)).split('b')[1])
        subnetmask = '.'.join(deafultsubnetmask)
        binsubjoin = ".".join(binsubnet)
        cidr = binsubjoin.count('1')
        print("ipcheck", binsubnet)
        print(f"Subnet mask will be {subnetmask}=/{cidr}")


Subnetor()
