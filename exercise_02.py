#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
#Помогите Кате отгадать задуманные Петей числа.

sum = int(input('Введите сумму загаданных чисел: '))
equal = int(input('Введите произведение загаданных чисел: '))

i = 0
j = 0

for i in range(equal):
    for j in range(equal):
        if i + j == sum and i * j == equal:
            print(i, j)
            break
