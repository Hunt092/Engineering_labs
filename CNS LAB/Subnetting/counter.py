def count(increament) :
    allAddress=[]
    hostAddress=[]
    finalhostAdd=[]
    for i in range (256):
        allAddress.append(i)
    for i in range(0,255,increament):
        hostAddress.append(allAddress[i+1:i+(increament-1)])
    for i in hostAddress:
        for j in i:
            finalhostAdd.append(str(j))
    #print(finalhostAdd, len(finalhostAdd))
    return finalhostAdd