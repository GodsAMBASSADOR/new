# Develop a program that converts between Fahrenheit and Celsius
# temperatures. Allow users to input a temperature and choose the
# conversion direction.

# (f - 32) * (5/9) = c
# (c * 9/5) + 32 = f
converted = 0
current_temp = float(input("Enter your current Temperature: "))
convert_to = (input("Enter 'C' to convert to celsius and 'F' to convert to Fahrenheit: ")).lower()
if convert_to == "c":
    converted = (current_temp - 32) * (5/9)
elif convert_to == "f":
    converted = (current_temp * 9/5) + 32

print(f'Converted temperature = {converted.__round__(3)} {convert_to}')
