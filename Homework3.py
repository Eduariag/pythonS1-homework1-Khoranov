 #Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число 
'''
N = abs(int(input('Введите количество элементов списка А: ')))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Число {X} встречается в списке A {count} раз') 
 '''   
    
#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

'''
N = abs(int(input('Number of List A items: ')))
A_entered = input(" List Items: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('The number of elements is more than stated!')
else:
    X = int(input('Enter the number to compare X: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f'Number {A_num[index]} in the list A is the closest {X} ')
    '''