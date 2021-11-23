# 4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, 
# обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def first_func():
    return "pi "

def second_func():
    return "= "

def third_func():
    return "3.14"

def result_func():
    result_str = ""
    result_str += first_func()
    result_str += second_func()
    result_str += third_func()
    print(result_str)

result_func()