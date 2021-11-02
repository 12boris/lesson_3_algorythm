"""извиняюсь за то, что сдаю ПР в виде ZIP-архива, я не успел просмотреть уроки на эту тему. Если кратко, я отдыхал.
следующее ПР сдам ввиде """

import random


"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

res = {}

for i in range(2, 10):
    res[i] = []

    for ii in range(2, 100):
        if ii % i == 0:
            res[i].append(ii)

    print(f'для числа {i} кратны {len(res[i])} чисел. именно: {res[i]}')


"""
2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается 
с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

first_mas = [8, 3, 15, 6, 4, 2]
second_mas = []

for i in first_mas:
    if i % 2 == 0:
        second_mas.append(first_mas.index(i))

print(second_mas)

for i in second_mas:
    print(first_mas[i])

"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

s = []

for i in range(random.randint(20, 25)):
    s.append(random.randint(1, 100))

print(s)

max_num = max(s)
min_num = min(s)
min_ind = s.index(min(s))
max_ind = s.index(max(s))
print(f'min: {min_num}, index: {min_ind}. max: {max_num}, index: {max_ind}')

del s[min_ind]
del s[max_ind]
s.insert(min_ind, max_num)
s.insert(max_ind, min_num)

print(s)

"""
4. Определить, какое число в массиве встречается чаще всего.
"""

s = [2, 3, 4, 5, 9, 5, 5, 6, 8, 6, 7, 6, 7, 6]
max_ind = 0
for_str = ['', '']

for i in s:
    if max_ind < s.count(i):
        max_ind = s.count(i)
        for_str[0] = s.count(i)
        for_str[1] = i
print(f'число {for_str[1]} встречается {for_str[0]} раза')

"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

s = [i for i in range(random.randint(-10, -5), random.randint(5, 10))]

"""
я не понимаю задачу. Здесь же можно просто написать: print(min(s))
"""

min_ = []
for i in s:
    if i < 0:
        min_.append(i)

if len(min_) > 0:
    print(min(min_))

else:
    print('отрицательных чисел нет.')

"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

s = []

for i in range(random.randint(20, 25)):
    s.append(random.randint(1, 100))

print(s)

max_num = max(s)
min_num = min(s)
min_ind = s.index(min(s)) + 1
max_ind = s.index(max(s)) - 1

s1 = s[min_ind:max_ind]
sum = 0
print(s1)

if len(s1) > 0:
    for i in s1:
        sum += i
    print(sum)
else:
    print('между ними нет чисел')

"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой 
(оба являться минимальными), так и различаться.
"""

s = []
for i in range(random.randint(20, 25)):
    s.append(random.randint(1, 100))

print(s)

first_min = min(s)
del s[s.index(first_min)]
second_min = min(s)

print(f'первое: {first_min}, второе: {second_min}')

"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

x = 5
y = [1, 2, 3, 4]
s = []
for i in y:
    b = []
    sum = 0
    print(f'{i}-ая строка:')

    for j in range(x-1):
        n = int(input())
        sum += n
        b.append(n)
    b.append(sum)
    s.append(b)

for i in s:
    print(i)

"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

x = 10
y = 5
s = []

for i in range(y):
    b = []

    for j in range(x):
        n = int(random.random()*200)
        b.append(n)
        print('%4d' % n, end='')
    s.append(b)
    print()

mx = -1

for j in range(x):
    mn = 200

    for i in range(y):
        if s[i][j] < mn:
            mn = s[i][j]

    if mn > mx:
        mx = mn
print()
print(f'Максимальный среди минимальных: {mx}')
