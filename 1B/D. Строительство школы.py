'''
D. Строительство школы

В деревне Интернетовка все дома расположены вдоль одной улицы по одну сторону от нее. По другую сторону от этой улицы пока ничего нет, но скоро все будет – школы, магазины, кинотеатры и т.д.

Для начала в этой деревне решили построить школу. Место для строительства школы решили выбрать так, чтобы суммарное расстояние, которое проезжают ученики от своих домов до школы, было минимально.

План деревни можно представить в виде прямой, в некоторых целочисленных точках которой находятся дома учеников. Школу также разрешается строить только в целочисленной точке этой прямой (в том числе разрешается строить школу в точке, где расположен один из домов – ведь школа будет расположена с другой стороны улицы).

Напишите программу, которая по известным координатам домов учеников поможет определить координаты места строительства школы.

Формат ввода
Сначала вводится число N — количество учеников (0 < N < 100001). Далее идут в строго возрастающем порядке координаты домов учеников — целые числа, не превосходящие 2 × 109 по модулю.

Формат вывода
Выведите одно целое число — координату точки, в которой лучше всего построить школу. Если ответов несколько, выведите любой из них.

Пример 1
Ввод	Вывод
4
1 2 3 4
3
Пример 2
Ввод	Вывод
3
-1 0 1
0
'''

n = int(input())

a = list(map(int, input().split(maxsplit = n)))

if n % 2 == 0:
    print(a[int(n/2)-1])
else:
    print(a[int((n-1)/2)])