'''Задание 1
Пользователь вводит с клавиатуры два числа. Нужно посчитать отдельно сумму четных, нечетных и чисел,
кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы'''
# n1=int(input('Введите первое число '))
# n2=int(input('Введите второе число '))
# sum_of_even=0
# count_even=0
# sum_of_odd=0
# count_odd=0
# sum_multiple_of_nine=0
# count_nine=0
# for i in range (n1,n2+1):
#     if i%2==0:
#         sum_of_even+=i
#         count_even+=1
#     else:
#         sum_of_odd+=i
#         count_odd+=1
#     if i%9==0:
#         sum_multiple_of_nine+=i
#         count_nine+=1
# if count_even !=0:
#     average_event=sum_of_even/count_even
# else:
#     average_event=0
# if count_odd !=0:
#     everage_odd = sum_of_odd/count_odd
# else:
#     everage_odd=0
# if count_nine !=0:
#     everage_nine= sum_multiple_of_nine/count_nine
# else:
#     everage_nine=0
# print('Сумма четных чисел:', sum_of_even, '\nCреднеарифметическое четных чисел:',average_event)
# print('Сумма нечетных чисел:', sum_of_odd, '\nCреднеарифметическое нечетных чисел:',everage_odd)
# print('Сумма кратных 9:', sum_multiple_of_nine, '\nCреднеарифметическое кратных 9:',everage_nine)
'''Задание 2
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. Нужно отобразить на экране вертикальную линию из введенного символа,
указанной длины. Например, если было введено 5 и символ %, тогда вывод на экран будет такой:'''
# number1= str(input("Введите символ: "))
# number2= int(input("Введите длину линии: "))
# for i in range(number2):
#     print(number1)
'''Задание 3
Пользователь вводит с клавиатуры числа. Если число больше нуля нужно вывести надпись «Numberis positive», если меньше 
нуля «Numberis negative», если равно нулю «Number is equal to zero». Когда пользователь вводит число 7 программа прекращает свою работу
и выводит на экран надпись «Good bye!»'''
# number= int(input("Введите число "))
# if number>0 and number!=7:
#     print('Numberis positive')
# elif number<0:
#     print('Numberis negative')
# elif number==0:
#     print('Number is equal to zero')
# elif number==7:
#     print('Good bye!')
'''Задание 4
Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
введенных чисел. Когда пользователь вводит число 7
программа прекращает свою работу и выводит на экран
надпись «Good bye!»'''
# sum = 0
# max = 0
# min = 0
# while True:
#     number = float(input("Введите число: "))
#     if number == 7:
#         print("Good bye!")
#         break
#         sum = sum + number
#     if number != 7:
#         sum = sum + number
#     if max == 0 or number > max:
#         max = number
#     if min == 0 or number < min:
#         min = number
# print ("Сумма введенных чисел = ", sum)
# print ("Максимум из введенных чисел = ", max)
# print ("Минимум из введенных чисел",min)

