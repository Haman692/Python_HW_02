# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import math

print('Сумма чисел')
sum = int(input())
print('Произведение чисел')
multy = int(input())
for i in range(sum):
    for g in range(multy):
        if (i + g == sum) and (i*g == multy):
            print('Петя загодал ' + str(i) + ' ' + str(g))
            break 
    if (i + g == sum) and (i*g == multy):
        break