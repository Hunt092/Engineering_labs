import counter
import ipchecker


def Subnetor():

    while True:
        ip = ipchecker.ipchecker()
        # checks
        ipchecks = bin(int(ip.split('.')[0])).split('b')[1]
        ipcut = str(ipchecks[:3])
        if ipcut == '110':
            ipsplit = ip.split('.')
            realip = str(ipsplit[0]+'.'+ipsplit[1]+'.'+ipsplit[2]+'.')

            # cutting out the last octet for operations on class c ip addresses
            lastoct = int(ipsplit[3])

            # getting the last octet for class c subnets mainly
            lastsub = 0
            ipblocks = [2, 4, 16, 32, 64, 128, 254]
            ipblockselector = 0
            selector = int(input('enter number of users per network:\n'))
            for i in ipblocks:
                if i >= selector:
                    ipblockselector = i
                    break
            # switch to select last 4bit of subnet
            if ipblockselector == 2:
                lastsub = 252
            elif ipblockselector == 4:
                lastsub = 248
            elif ipblockselector == 16:
                lastsub = 240
            elif ipblockselector == 32:
                lastsub = 224
            elif ipblockselector == 64:
                lastsub = 192
            elif ipblockselector == 128:
                lastsub = 128
            elif ipblockselector == 254:
                lastsub = 0

            subnet = '255.255.255.'+str(lastsub)
            subnetsplit = subnet.split('.')

            binsubnet = []
            for i in subnetsplit:
                binsubnet.append(bin(int(i)).split('b')[1])
            binsubjoin = ''.join(binsubnet)
            cidr = binsubjoin.count('1')
            print("ipcheck", subnetsplit)
            print("ipcheck", binsubnet)

            print(
                f'you needed a network that can accommodate  {selector}  nodes in a network\n\nyou would probably use this subnet mask:\n {subnet} = /{cidr}')
            while True:
                option = input(
                    'wanna go ahead and print the ip address (y/n)?:\t')
                if option == 'y':
                    subSplit = subnet.split('.')

                    if (0 <= int(subSplit[1]) < 255):
                        print('subnetting in the second octet')
                        binoctet = bin(int(subSplit[1])).split('b')[1]
                        print(binoctet)
                        increament = 256-int(subSplit[1])
                        print(increament)
                        counter.count(increament)

                    elif (0 <= int(subSplit[2]) < 255):
                        print('subnetting in the third octet')
                        binoctet = bin(int(subSplit[2])).split('b')[1]
                        # print(binoctet)
                        increament = 256 - int(subSplit[2])
                        # print(increament)
                        counter.count(increament)

                    elif (0 <= int(subSplit[3]) < 255):
                        print('subnetting in the last octet')
                        binoctet = bin(int(subSplit[3])).split('b')[1]
                        # print(binoctet)
                        increament = 256 - int(subSplit[3])
                        # print(increament)
                        iplist = counter.count(increament)

                        for ip in iplist:
                            if int(ip) > lastoct:
                                print(realip+str(ip))

                else:
                    print('thank you for using my application bye\n')
                    import time
                    time.sleep(2)
                    print('exiting.......')
                    exit()


Subnetor()
