# reversing a string

from audioop import reverse


def reversed_word(word):
    return word[::-1]

my_word = reversed_word(input('Enter Word to reverse: '))

print(my_word)

#Capitalize Letters
letter = input('What is your favorite thing to do: ')

cap_word = letter.title()
print (cap_word)

#compressing a string of characters

def solve(compress):