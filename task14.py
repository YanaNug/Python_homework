# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# k = 1
# n = int(input('N: '))

# for i in range(k, n+1):
#     print(f'2 в степени {i} = {2**i}')


n = int(input('N: '))
k=1
while k<=n:
    print(k,end=' ')
    k=k*2
        
