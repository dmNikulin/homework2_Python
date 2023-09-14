#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input('Введите число: '))

if num < 0:
    num = num * (-1)

step = 0
x = 2
result = 1

while result < num:
   result = pow(x, step)
   if result < num:
       print(result)
   step += 1
