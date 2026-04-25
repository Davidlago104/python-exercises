#Basic Calculator
num1 = float(input("Give me a number "))
num2 = float(input("Give me a second Number "))

def add():
    total = num1 + num2
    print("Adding %d and %d, your total is %d" % (num1, num2, total))
add()

def divide():
    total = num1 / num2
    print("Dividing %d and %d, your total is %d" % (num1, num2, total))
divide()

def multi():
    total = num1 * num2
    print("Multiplying %d and %d, your total is %d" % (num1, num2, total))
multi()

def power():
    total1 = num1 ** 2
    total2 = num2 ** 2
    print("Squaring both numbers (%d, %d) gives you %d and %d5" % (num1, num2, total1, total2))
power()
