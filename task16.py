# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X


n = int(input())
arr = [int(i) for i in input().split()]
x = int(input())
count = 0
for i in arr:
    if i == x:
        count += 1
print(f'В заданном массиве {arr} число {x} встречается {count} раз(а).')