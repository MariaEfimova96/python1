'''Задание 1:
Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
Необходимо вывести на экран результат выражения. В нашем примере это 35. Арифметическое выражение
может состоять только из трёх частей: число, операция, число. Возможные операции: +, -,*,/'''
# import operator
# expression =(input("Введите арифметическое выражение (ввод значений через пробел): "))
# operators = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv
# }
# operands = expression.split()
# first_operand = float(operands[0])
# operator_symbol = operands[1]
# second_operand = float(operands[2])
# if operator_symbol in operators:
#     result = operators[operator_symbol](first_operand, second_operand)
#     print("Результат выражения: ", result)
# else:
#     print("Неверная операция")
'''В списке целых, заполненном случайными числами,
определить минимальный и максимальный элементы, посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.'''
# import random
# list = [random.randrange(-4000, 9000) for i in range(10)]
# print ("Список случайных чисел: " +  str(list))
# a = max(list)
# print("Максимальное число: ", a)
# b = min(list)
# print("Минимальное число: ", b)
# i = 0
# print('Кол-во положительных элементов:', sum(i > 0 for i in list))
# print('Кол-во отрицательных элементов:', sum(i < 0 for i in list))
# print('Кол-во нулей:', sum(i == 0 for i in list))