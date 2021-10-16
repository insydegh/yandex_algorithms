'''
C. Уникальные элементы
Ограничение времени	3 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.

Пример 1
Ввод	Вывод
1 2 2 3 3 3
1
Пример 2
Ввод	Вывод
4 3 5 2 5 1 3 5
4 2 1
'''

a = list(map(int, input().split()))
b = list()
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(*b)