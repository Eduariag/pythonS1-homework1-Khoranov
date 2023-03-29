#Напишите программу, которая на вход принимает два числа A и B,
#и возводит число А в целую степень B с помощью рекурсии.
'''
def recApowB(a, b):
    if b == 0:
        return 1
    return a * recApowB(a, b - 1)

a = int(input('enter a number: '))
b = int(input('enter the degree: '))
print(recApowB(a, b))
'''

#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
#Также нельзя использовать циклы.
'''
def recsum(a, b):
    if b == 0:
        return a
    return 1 + recsum(a, b - 1)

print(recsum(2, 2))
'''