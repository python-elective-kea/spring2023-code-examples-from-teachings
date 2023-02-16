
l = []
for i in range(10):
    l.append(i)


li_comp = [ i for i in range(15) ]


# Create a list of capital letters in the english alphabet

import string

cap_let = [i for i in string.ascii_uppercase]


cap_letter_dino = []


for i in range(65, 91):
    cap_letter_dino.append(chr(i))


cap_letter_comp = [chr(i) for i in range(65, 91)]


# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.



ex2 = [chr(i) for i in range(65, 91) if i not in range(70, 86, 5)]


#Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

ex3 = [chr(i) for i in range(65, 91) if i not in range(70, 80, 5)]

l = [1, 2, 3, 4, 5]


# Nested list comprehensions


# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1) ....]

l = []
for i in range(3):
    for j in range(2):
         l.append((i, j))


li_nested = [(i,j) for i in range(3) for j in range(2) ]


ll = [i if i%2==0 else 'HELLO' for i in range(10)]


# clothes exercise

colors = ('Black', 'White')
sizes = ('s', 'm', 'l', 'xl')


clothes = [(c,s) for c in colors for s in sizes]

# exclude


clothes_new = [(c,s) for c in colors for s in sizes if (c,s) not in [('Black', 'm'), ('White', 'm')]]





clothes_new = [(c,s) for c in colors for s in sizes if(c,s) not in [('Black', 'm'), ('White', 'm')]]




## SYS exercise


import sys

def greeting(x):

    if len(x) == 2 and x[1] == '-it':
        print('interactive terminal started')
    if len(x) == 3 and x[2] == '--rm':
        print('Will be removed at exit')

    if len(x) == 1:
        print('Usage: python script.py [-it]{--rm}')

greeting(sys.argv)





























































































