# Program to check if a number is Armstrong Number
number = int(input('Enter a number that you want to check if its a Armstrong Number : '))
stringValue = str(number)
power = len(stringValue)

result = 0
i = 1
while i < power+1:
    result += int(stringValue[i-1])**power
    i += 1

if result == number:
    print("Hurray!!, The entered number {0} is an Armstrong Number.".format(number))
else:
    print("Sorry, The entered number {0} is NOT an Armstrong Number.".format(number))
