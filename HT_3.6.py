# 6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
# -  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
# -  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
# -  якщо довжина бульше 50 - > ваша фантазiя - > розділити числа на парні та непарні

def check_func(str_input):

    letters_numbers = []
    letters = []
    numbers = []
    
    for i in str_input:
        letters_numbers.append(i)
    for i in letters_numbers:
        if i.isdigit():
            numbers.append(int(i))
        else:
            letters.append(i)

    if len(str_input) > 30 and len(str_input) < 50:
        print(len(str_input))
        print(len(letters))
        print(len(numbers))

    if len(str_input) < 30:
        print(sum(numbers))
        print("".join(letters))

    if len(str_input) > 50:
        paired_numbers = []
        unpaired_numbers = []
        for i in numbers:
            if i % 2 == 0:
                paired_numbers.append(i)
            else:
                unpaired_numbers.append(i)
        print("Парні: " + str(paired_numbers))
        print("Непарні: " + str(unpaired_numbers))


check_func("fsdgfddf645546")

