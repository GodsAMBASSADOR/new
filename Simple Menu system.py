# Simple Menu System with while Loop:
# Build a program with a menu system that allows the user to choose from
# the following options:
# Calculate Sum:
# When the user selects this option, the program should prompt them to
# enter a series of numbers separated by spaces and then calculate and
# display the sum of those numbers.
# Search for a Word:
# If the user selects this option, the program should ask the user to enter a
# sentence or text. Then, prompt them to enter a word to search for within
# that text and display whether or not the word is found in the text.
# Quit:
# This option allows the user to exit the program.
# Use a while loop to keep the program running until the user chooses to quit.
print('''> To Calculate Sum, type 'sum'
> To Search for a Word, type 'search'
> To quit, type 'q' ''')
while True:
    menu = input('What did you want to do: ').lower()
    if menu == 'q':
        break
    elif menu == 'sum':
        option = input('Enter the number, separate then with space: ').split()
        total = 0
        for integers in option:
            total += int(integers)
        print(f'Total = {total}')
    elif menu == 'search':
        option = input('Enter a sentence or text: ').split()
        word = input('Enter a word to search for within the text: ')
        if word in option:
            print(f'{word} is in the text')
        else:
            print(f'{word} is not the text')
