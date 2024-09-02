'''Задание 1
Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все
числа в этом диапазоне по следующему правилу: если число кратно 7, его надо выводить на экран.'''
# number1= int(input("Введите первое число: "))
# number2= int(input("Введите второе число: "))
# print('Числа кратные 7')
# if number2 > number1:
#     for i in range(number1, number2 + 1):
#         if i % 7 == 0:
#             print(i, end=" ")
# if number1 > number2:
#     for i in range(number2, number1 + 1):
#         if i % 7 == 0:
#             print(i, end=" ")
'''Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать все числа в этом диапазоне. Нужно вывести на экран: 
1. Все числа диапазона;
2. Все числа диапазона в убывающем порядке;
3. Все числа, кратные 7;
4. Количество чисел, кратных 5.'''
# number1= int(input("Введите первое число: "))
# number2= int(input("Введите второе число: "))
# print('Все числа диапазона')
# if number2 > number1:
#     for i in range(number1, number2 + 1):
#         print(i, end=" ")
# elif number1 > number2:
#     for i in range(number2, number1 + 1):
#         print(i, end=" ")
# print('\nВсе числа в порядке убывания')
# if number1 > number2:
#     for i in range(number1, number2-1,-1):
#         print(i, end=" ")
# elif number2 > number1:
#     for i in range(number2, number1-1,-1):
#         print(i, end=" ")
# print('\nЧисла кратные 7')
# if number2 > number1:
#     for i in range(number1, number2 + 1):
#         if i % 7 == 0:
#             print(i, end=" ")
# elif number1 > number2:
#     for i in range(number2, number1 + 1):
#         if i % 7 == 0:
#             print(i, end=" ")
# print('\nКоличество чисел кратных 5')
# count = 0
# for i in range(number1, number2 + 1):
#         if i%5==0:
#             count= count +1
# print(count)
'''Задание 3
Пользователь вводит с клавиатуры два числа (начало и конец диапазона) Требуется проанализировать все числав этом диапазоне. 
Вывод на экран должен проходить по правилам, указанным ниже.
Если число кратно 3 (делится на 3 без остатка) нужно вывести слово Fizz. Если число кратно 5 нужно вывести слово Buzz. Если число кратно 3 и 5 нужно вывести
Fizz Buzz. Если число не кратно не 3 и 5 нужно вывести само число.'''
# number1= int(input("Введите первое число: "))
# number2= int(input("Введите второе число: "))
# for i in range(number1, number2 + 1):
#     if i %3==0 and i %5==0:
#         print('Fizz Buzz', end=",")
#     elif i%3==0:
#         print('Fizz', end=",")
#     elif i%5==0:
#         print('Buzz', end=",")
#     else:
#         print(i, end=",")