'''Задание 1
Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
“Don't compare yourself with anyone in this world…
if you do so, you are insulting yourself.” Bill Gates'''
# def formatted_text():
# #Вводим переменную с необходимым текстом
#     text = ('"Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself."\n                                          Bill Gates'
#     )
#     print(text)
# #Вызов функции
# formatted_text()
'''Задание 2
Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.'''
# def number(start_number, stop_number):
#     step = 1
#     if start_number > stop_number:
#         step = -1
#     for i in range(start_number, stop_number + step, step):
#         if i % 2 == 0:
#             print(i, end=' ')
# number(33, 7)
'''Задание 3
Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа. Функция принимает в качестве параметров: длину стороны квадрата, 
символ и переменную логического типа:
■ если она равна True, квадрат заполненный;
■ если False, квадрат пустой'''
# def square(line,symbol, result):
#     for i in range(line):
#         if result or i == 0 or i == (line - 1):
#             print(symbol * line)
#         else:
#             print(symbol + (' ' * (line - 2)) + symbol)
#
# square(7, '@', False)
#
#
# square(7, '$', True)
'''Задание 4
Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров.'''
# def min_numbers (a,b,c,d,e):
#     return min(a,b,c,d,e)
# min_value = min_numbers(-1, 7, 0, 22, 4)
# print("Минимальное число:", min_value)
'''Задание 5
Напишите функцию, которая возвращает произведение чисел в указанном диапазоне. Границы диапазона
передаются в качестве параметров. Если границы диапазона перепутаны например, 5 верхняя граница, 25-нижняя граница)
 их нужно поменять местами.'''
# def number_product (lower, upper):
#     if lower > upper:
#         lower, upper = upper, lower
#     product=1
#     for i in range(lower, upper + 1):
#         product *= i
#     return product
# result = number_product(3, 7)
# print("Произведение чисел в диапазоне:", result)
#
# result = number_product(7, 3)
# print("Произведение чисел в диапазоне:", result)
'''Задание 6
Напишите функцию, которая считает количество цифр в числе. Число передаётся в качестве параметра. Из функции нужно вернуть полученное количество цифр.
Например, если передали 3456, количество цифр будет 4.'''
# def count_digits(number):
#     # Преобразуем число в строку и считаем количество цифр
#     return len(str(abs(number)))
# digit_count = count_digits(3456)
# print("Количество цифр:", digit_count)
'''Напишите функцию, которая проверяет является ли
число палиндромом. Число передаётся в качестве параметра. Если число палиндром нужно вернуть из функции
true, иначе false. «Палиндром» — это число, у которого первая часть цифр равна второй перевернутой части цифр. Например, 
123321—палиндром(первая часть 123, вторая 321, которая
после переворота становится 123), 546645 — палиндром,
а 421987 — не палиндром. '''
# def palindrome(number):
# # Преобразуем число в строку
#     num_str = str(number)
# # Сравниваем строку с её обратной версией
#     return num_str == num_str[::-1]
# print(palindrome(123321))  # True
# print(palindrome(546645))  # True
# print(palindrome(421987))  # False



