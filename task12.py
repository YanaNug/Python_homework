# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# x = int(input('X: '))
# y = int(input('Y≤1000: '))
# if y >=1000:
#     print('Не соответсвует условию! Введите Y ≤ 1000')
# else:
#     print(f'Сумма загаданных чисел = {x + y}')
#     print(f'Произведение загаданных чисел = {x * y}')

# x_1 = int(input('Введите отгаданное число х: '))
# y_1 = int(input('Введите отгаданное число y: '))
# if x == x_1 and y == y_1:
#     print('Загаданные числа отгаданы верно!')
# else: 
#     print('Загаданные числа отгаданы не верно!')

                                            #or

sum = int(input('Сумма загаданных чисел: '))
proizv = int(input('Произведение загаданных чисел: '))

x = int(input('Введите отгаданное число X: '))
y = int(input('Введите отгаданное число Y≤1000: '))
if y >= 1000:
    print('Не соответсвует условию! Введите Y ≤ 1000')
elif sum == x + y and proizv == x * y:
    print('Загаданные числа отгаданы верно!')
else:
    print('Загаданные числа отгаданы не верно!')