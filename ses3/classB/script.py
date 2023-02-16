l = []
for i in range(10):
    l.append(i)

# list comprehension

li_comp = [i for i in range(15) ]



# Create a list of capital letters in the english alphabet

import string

letters = list(string.ascii_uppercase)

# 2. solution
let = [chr(letter) for letter in range(ord('A'), ord('Z')+1)]

let = [chr(letter) for letter in range(65, 91)]



letters = 'A B C D'.split()




# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.


let = [chr(letter) for letter in range(65, 91) if letter not in (70, 75, 80, 85)]

tu = 70, 75, 80, 85


let = [chr(letter) for letter in range(65, 91) if letter not in range(70, 80, 2)]


# nested for loop

# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1) ....]

l = []

for i in range(3):
    for j in range(2):
        l.append((i,j))
        

li_comp = [(i,j) for i in range(3) for j in range(2)]


# clothes

colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

# [('Black', 's'), ('Black', 'm'), ('Black', 'l'), ('Black', 'xl'), ('White', 's'), ('White', 'm'), ('White', 'l'), ('White', 'xl')]


clothes = [(c,s) for c in colors for s in sizes]

x = [('Black', 'm'), ('White', 'm')]

clothes = [(c,s) for c in colors for s in sizes if (c,s) not in x]













































