# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculate(first_num, second_num, operation):
    operation_list = ["+", "-", "/", "*"]
    if str(first_num).isdigit() and str(second_num).isdigit() and operation in operation_list:
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
        print("You can do only this operation(+, -, /, *) with numbers, please, change your input")

#operation_list = ["+", "-", "/", "*"]
#first_num = input("Write first number: ")
#second_num = input("Write second number: ")
#operation = input("Write operation to do: ")

calculate(5,8,+)