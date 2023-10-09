# Write a program that prints the numbers from 1 to N, where N is  user defined
# positive integer. But for multiples of 3, print "Fizz" instead of the
# number, and for multiples of 5, print "Buzz" instead of the number. For
# numbers which are multiples of both 3 and 5, print "FizzBuzz."

num = int(input("Enter a positive integer N: "))
for integer in range(1, num + 1):
    if integer % 3 == 0 and integer % 5 == 0:
        print("FizzBuzz")
    elif integer % 3 == 0:
        print("Fizz")
    elif integer % 5 == 0:
        print("Buzz")
    else:
        print(integer)
