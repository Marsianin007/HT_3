# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculations(first_num, operation, second_num):
    operation_list = ["+", "-", "/", "*"]
    if first_num.isdigit() and second_num.isdigit() and operation in operation_list and int(second_num) != 0:
        first_num = int(first_num)
        second_num = int(second_num)

        if operation == "+":
            print(str(first_num) + " + " + str(second_num) + " = " + str(first_num + second_num))
        if operation == "-":
            print(str(first_num) + " - " + str(second_num) + " = " + str(first_num - second_num))
        if operation == "*":
            print(str(first_num) + " * " + str(second_num) + " = " + str(first_num * second_num))
        if operation == "/":
            print(str(first_num) + " / " + str(second_num) + " = " + str(first_num / second_num))
    else:
        print("You can do only this operation(+, -, /, *) with numbers except '0', please, change your input")

def calculate():
    first_num = input("Write first number: ")
    operation = input("Write operation to do: ")
    second_num = input("Write second number: ")
    calculations(first_num, operation, second_num)

calculate()