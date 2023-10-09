# Build a calculator that can perform various operations (addition, subtraction,
# multiplication, division, exponentiation, floor division) based on user input.
# Use functions and a menu system to allow the user to choose the operation.

print("Welcome to calculator. \nFollow the prompts to get your calculations")
menu = ('\n'
        'Note: For addition, press + \nFor subtraction, press -\nFor multiplication, press * \n'
        'For division, press / \nFor exponentiation, press ** \nFor floor division, press //\n'
        'Press = to stop calculations'
        '\n')
message = "Check to input the correct symbol"
print(menu)
num = float(input('Enter the first number: '))
total = 0
symbol = input('Enter the symbol: ')
num2 = float(input('Enter the next number: '))
if symbol == '+':
    total = num + num2
    print(total)
elif symbol == '-':
    total = num - num2
    print(total)
elif symbol == '*':
    total = num * num2
    print(total)
elif symbol == '/':
    total = num / num2
    print(total)
elif symbol == '**':
    total = num ** num2
    print(total)
elif symbol == '//':
    total = num // num2
    print(total)
else:
    print(message)


while True:
    symbol = input('Enter the symbol: ')
    if symbol == '=':
        break
    num2 = float(input('Enter the next number: '))
    if symbol == '+':
        total += num2
        print(total)
    elif symbol == '-':
        total -= num2
        print(total)
    elif symbol == '*':
        total *= num2
        print(total)
    elif symbol == '/':
        total /= num2
        print(total)
    elif symbol == '**':
        total **= num2
        print(total)
    elif symbol == '//':
        total //= num2
        print(total)
    else:
        print(message)
