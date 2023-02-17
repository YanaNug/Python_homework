# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# a = input('A = ')
# b = input('B = ')

def stepen_num(a, b):
    result = 1;
    i = 1;
    while i<=b:   
        result = result * a
        i +=1
    print(result)

stepen_num(int(input('a = ')), int(input('b = ')))