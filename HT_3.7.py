# 7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!

def calculate(first_num, second_num, operation):
    if operation == "+":
        print(str(first_num) + " + " + str(second_num) + " = " + str(first_num + second_num))
    if operation == "-":
        print(str(first_num) + " - " + str(second_num) + " = " + str(first_num - second_num))
    if operation == "*":
        print(str(first_num) + " * " + str(second_num) + " = " + str(first_num * second_num))
    if operation == "/":
        print(str(first_num) + " / " + str(second_num) + " = " + str(first_num / second_num))

first_num = int(input("Write first number: "))
second_num = int(input("Write second number: "))
operation = input("Write operation to do: ")

calculate(first_num, second_num, operation)