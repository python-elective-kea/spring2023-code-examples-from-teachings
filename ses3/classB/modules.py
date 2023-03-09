import sys

def greeting(x):

    if len(x) == 2 and x[1] == '-it':
        print('interactive terminal started')
    if len(x) == 3 and x[2] == '--rm':
        print('Will be removed at exit')
    else:
        print('Usage: python script.py [-it]{--rm}')
greeting(sys.argv)




import requests


f = requests.get('https://www.kea.dk')
