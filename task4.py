# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input('Введите количество журавликов сделанных Петей, Катей и Сережей вместе: '))

k = int((s*2)/3)
p = int((k/2)/2)
c = int(p)

print(p, k, c)