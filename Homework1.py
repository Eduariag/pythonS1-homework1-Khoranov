#Задача1 
#Сумма чисел трехзначного числа
'''
n=int(input('enter a three-digit number:  '))
a=n%10
b=n%100//10
c=n//100
print("the sum of the digits of the number:" , a+b+c)
'''

#Задача 2 Сколько всего журавликов сделают
'''
a=int(input('Количество журавликов Сережи:  '))
b=a
c=(a+b)*2
print(a+b+c)
'''

#Задача 3 Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех
'''
num=input('enter a three-digit number:  ')
sum_1 = int(num[0]) + int(num[1]) + int(num[2]) 
sum_2 = int(num[3]) + int(num[4]) + int(num[5])
if sum_1 == sum_2:
    print('Счастливый')
else:
    print('Обычный')
'''

#Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек отломить k 
# долек, если разрешается сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).