# Create a program that checks if a given string is a palindrome using a
# function. Allow the user to input the string and print the result.

word = input("Enter the word: ")
if word[::-1] == word:
    print(f' The word "{word}" is palindrome')
else:
    print(f' The word "{word}" is not palindrome')
