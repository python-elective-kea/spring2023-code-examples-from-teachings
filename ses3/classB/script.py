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


























