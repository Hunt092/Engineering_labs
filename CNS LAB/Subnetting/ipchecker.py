def ipchecker():
    while True:
        ip = input('enter a valid ip address:\n')
        a = ip.split('.')
        try:
            if ((len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255) and (0 <= int(a[2]) <= 255) and (0 <= int(a[3]) <= 255)):
                print('Valid C Class ip address')
                break
        except:
            print('please enter an integer')
        else:
            if (int(a[0]) == 127):
                answer = input('this is local host do you wish to continue')
                if answer == 'yes' or answer == 'y':
                    continue
                else:
                    break
            print('bad ip')
            continue
    return ip
