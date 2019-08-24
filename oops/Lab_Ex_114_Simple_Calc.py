# A Simple Calculator using class and oops - Multiple inheritance
class Addition:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02

    def add(self):
        """
        This function takes two numbers as input and returns their sum
        :param num1: the first number
        :param num2: the second number
        :return: the sum of first and second number
        """
        return self.number01 + self.number02


class Subtraction:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02

    def diff(self):
        """
        This function takes two numbers as input and returns their difference
        :return: the difference of first and second number
        """
        return self.number01 - self.number02


class Division:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02

    def division(self):
        """
        This function takes two numbers as input and returns the answer of first number divided by the second
        :return: the value of first number divided by the second number
        """
        return self.number01 / self.number02


class FloorDivision:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02

    def floor_division(self):
        """
        This function takes two numbers as input and returns the whole number of first number divided by the second
        :return: the value of first number divided by the second number
        """
        return self.number01 // self.number02


class Multiplication:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02

    def multiply(self):
        """
        This function takes two numbers as input and returns the answer of first number multiplied by the second
        :return: the value of first number multiplied by the second number
        """
        return self.number01 * self.number02


class Modulus:
    def __init__(self, number01, number02):
        self.number01 = number01
        self.number02 = number02

    def mod(self):
        """
        This function takes two numbers as input and returns the balance after perfectly dividing first
        number by the second number
        :return: the balance after perfectly dividing first number by the second
        """
        return self.number01 % self.number02


def print_menu():
    print(
        '''
        ---------------- CALCULATOR MENU ----------------

          1 - Add
          2 - Subtract
          3 - Multiply
          4 - Divide
          5 - Floor Division
          6 - Modulo
          7 - All

        -------------------------------------------------
    
        '''
    )


class Calculator(Addition, Subtraction, Division, Multiplication, FloorDivision, Modulus):
    pass


print_menu()
choice = int(input('Enter Your menu Choice - '))
num01 = int(input('Enter the First Number - '))
num02 = int(input('Enter the Second Number - '))
value = 0

if choice == 1:
    my_object = Addition(num01, num02)
    value = my_object.add()
elif choice == 2:
    my_object = Subtraction(num01, num02)
    value = my_object.diff()
elif choice == 3:
    my_object = Multiplication(num01, num02)
    value = my_object.multiply()
elif choice == 4:
    my_object = Division(num01, num02)
    value = my_object.division()
elif choice == 5:
    my_object = FloorDivision(num01, num02)
    value = my_object.floor_division()
elif choice == 6:
    my_object = Modulus(num01, num02)
    value = my_object.mod()
elif choice == 7:
    my_object = Calculator(num01, num02)
    value = {
        "Addition = ": my_object.add(),
        "Subtraction = ": my_object.diff(),
        "Division = ": my_object.division(),
        "Floor Division = ": my_object.floor_division(),
        "Modulus = ": my_object.mod(),
        "Multiplication = ": my_object.multiply()
    }
else:
    print('Invalid menu choice')

print('Result = ', value)
