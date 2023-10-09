# Write a program that takes a user-inputted integer and performs the
# following tasks:
# Check if it's even or odd.
# Determine if it's a prime number.
# Calculate its factorial.

num = int(input("Enter the number: "))
total = 1
prime_list = []
factorial_num = num
print(f'{num} is Even') if num % 2 == 0 else print(f'{num} is odd')
for i in range(1, num + 1):
    if num % i == 0:
        prime_list.append(i)
if prime_list == [1, num]:
    print(f'{num} is a Prime number')
else:
    print(f'{num} is not a prime number')

while num != 0:
    total *= num
    num -= 1
print(f'The factorial of {factorial_num} is {total}')

