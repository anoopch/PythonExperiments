# Program to find if the entered number is divisible by another number
def division_checker(num, div):
    return num % div == 0


print('-------------------- MENU --------------------\n\n',

      '\t\t1 - Decimal to Hexadecimal ',
      '\n\t\t2 - Decimal to Binary ',
      '\n\t\t3 - Decimal to Octal ',

      '\n\t\t4 - Hexadecimal to Decimal',
      '\n\t\t5 - Hexadecimal to Binary',
      '\n\t\t6 - Hexadecimal to Octal',

      '\n\t\t7 - Binary to Decimal',
      '\n\t\t8 - Binary to Hexadecimal',
      '\n\t\t9 - Binary to Octal',

      '\n\t\t10 - Octal to Decimal',
      '\n\t\t11 - Octal to Hexadecimal',
      '\n\t\t12 - Octal to Binary',

      '\n----------------------------------------------')
choice = int(input('Enter Your menu Choice - '))
inputData = int(input('Enter the Number to convert - '))
value = 0
decimalValue = 8

if choice == 2 or choice == 5 or choice == 12:
    value = bin(inputData)
elif choice == 4 or choice == 7 or choice == 10:
    value = int(inputData, decimalValue)
elif choice == 1 or choice == 8 or choice == 11:
    value = hex(inputData)
elif choice == 3 or choice == 6 or choice == 9:
    value = oct(inputData)

print(value)

#
# elif choice == 2:
# elif choice == 2:
# elif choice == 2:
