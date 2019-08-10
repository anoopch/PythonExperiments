# Program to generate Fibonacci numbers
number = int(input('How many Fibonacci number do you want to generate? : '))

fibonacciList = [0, 1]

i = 0
while i < number:
    fibonacciList.append(fibonacciList[i] + fibonacciList[i + 1])
    i += 1

print("The first {0} fibonacci Numbers are as below.\n{1}".format(number, fibonacciList))
