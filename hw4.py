# Вычислить число c заданной точностью d
# Пример:  - при d = 0.001, π = 3.141 
#         10^{-1} ≤ d ≤10^{-10}


import math
d = input('Введите точность: ')

len_d = len(d) - 2
print(f"pi = {math.pi:.{len_d}f}")

  

# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N. 


n = int(input('Введите натуральное число: '))
if n > 0:
    multipliers = []
    while n > 1:
        for i in range(2, n + 1):
            count = True
            for j in range(2, i):
                if i % j == 0:
                    count = False
                    break
            if count:
                while n % i == 0:
                    multipliers.append(i)
                    n /= i
    print(multipliers)
else:
    print('Введено не натуральное число')

#  Решения не мои,прошу прощения..

# Задайте последовательность чисел. Напишите 
# программу, которая выведет список неповторяющихся
# элементов исходной последовательности.



# Задана натуральная степень k. Сформировать случайным
#  образом список коэффициентов (значения от 0 
# до 100) многочлена и записать в файл многочлен 
# степени k.
# Пример:k=2 => 2*x² + 4*x + 5 = 0 или 
#        x² + 5 = 0 или 10*x² = 0
# k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0




# Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл,
#  содержащий сумму многочленов.