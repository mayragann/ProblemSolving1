# # reversing a string

# from audioop import reverse


# def reversed_word(word):
#     return word[::-1]

# my_word = reversed_word(input('Enter Word to reverse: '))

# print(my_word)

# #Capitalize Letters
# letter = input('What is your favorite thing to do: ')

# cap_word = letter.title()
# print (cap_word)

# #compressing a string of characters

# def compress(string):
#     index = 0
#     compressed = ""
#     len_str = len(string)
#     while index != len_str:
#         count = 1
#         while (index < len_str-1) and (string[index] == string[index+1]):
#             count = count + 1
#             index = index + 1
#         if count == 1:
#             compressed += str(string[index])
#         else:
#             compressed += str(string[index]) + str(count)
#         index = index + 1
#     return compressed
       
 
# string = "aaaaaaaaaaabbbbbbbbbbbbcccccccccccffffffffffffffjjjjjj"
# print(compress(string))

def is_palindrome():
    def palindrome(word):
    
        reversed_word = word[::-1]
        status = 1
        if word != reversed_word:
            status =0
        return status

    word = input("Enter a Polindrome word: ")
    status = palindrome(word)

    if status == 1:
        print("That is a palindrome!")
          
    else:
        print("Sorry! Try again")
        is_palindrome()   
       
correct = is_palindrome() 
      