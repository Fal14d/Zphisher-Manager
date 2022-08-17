import time


def s(arg):
    time.sleep(arg)

load = '''
    Pick Data Type:
    
    |01$ Facebook      |11$ Twitch     |21$ DeviantArt
    |02$ Instagram     |12$ Pinterest  |22$ Badoo
    |03$ Google        |13$ Snapchat   |23$ Origin
    |04$ Microsoft     |14$ Linkedin   |24$ DropBox	
    |05$ Netflix       |15$ Ebay       |25$ Yahoo		
    |06$ Paypal        |16$ Quora      |26$ Wordpress
    |07$ Steam         |17$ Protonmail |27$ Yandex			
    |08$ Twitter       |18$ Spotify    |28$ StackoverFlow
    |09$ Playstation   |19$ Reddit     |29$ Vk
    |10$ Tiktok        |20$ Adobe      |30$ XBOX
    |31$ Mediafire     |32$ Gitlab     |33$ Github
    |34$ Discord|
    |99$ About         |00$ Exit       |69$ All Types (Longer Runtime)
'''
print(load)

try:
    Gena = int(input('Number: '))
    # gather table information for resource
except:
    print('Sorry, please select a int value: ')

if Gena == 1:
    print('Loading Data Prospector [1/3] ')
    s(1)
    Loader = 'Loaders.1.main'
    print('Importing data [2/3]')
    s(1.43)
    import Loaders.A.main
    print('Launching loader [3/3]')
    s(0.7)
    print('Commands Sending (1/2)')
    s(2.3)
    exec('Loaders.A.main.a()')
    print('Pipeline assured (2/2)')
    s(3.4)
    print('\n' * 50)
    exec('Loaders.A.main.B()')
    exec('Loaders.A.main.C()')
    exec('Loaders.A.main.D()')
    exec('Loaders.A.main.E()')
elif Gena == 2:
    print('Loading Data Prospector [1/3] ')
    s(1)
    Loader = 'Loaders.B.main'
    print('Importing data [2/3]')
    s(1.43)
    import Loaders.B.main

    print('Launching loader [3/3]')
    s(0.7)
    print('Commands Sending (1/2)')
    s(2.3)
    exec('Loaders.B.main.a()')
    print('Pipeline assured (2/2)')
    s(3.4)
    print('\n' * 50)
    exec('Loaders.B.main.B()')
    exec('Loaders.B.main.C()')
    # exec('Loaders.B.main.D()')
    # exec('Loaders.B.main.E()')
