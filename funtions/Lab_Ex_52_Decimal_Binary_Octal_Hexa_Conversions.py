# Program to Convert among Decimal, Binary, Octal, Hexadecimal using built in functions

print('-------------------- CONVERSION MENU --------------------\n\n',

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

      '\n-----------------------------------------------------')
choice = int(input('Enter Your menu Choice - '))
inputData = input('Enter the Number to convert - ')

value = 0

if choice == 1:
    value = hex(int(inputData))
elif choice == 2:
    value = bin(int(inputData))
elif choice == 3:
    value = oct(int(inputData))
elif choice == 4:
    value = int(inputData, 16)
elif choice == 5:
    value = bin(int(inputData, 16))
elif choice == 6:
    value = oct(int(inputData, 16))
elif choice == 7:
    value = int(inputData, 2)
elif choice == 8:
    value = hex(int(inputData, 2))
elif choice == 9:
    value = oct(int(inputData, 2))
elif choice == 10:
    value = int(inputData, 8)
elif choice == 11:
    value = hex(int(inputData, 8))
elif choice == 12:
    value = bin(int(inputData, 8))
else:
    print('Invalid menu choice')

print("Result = ", value)
