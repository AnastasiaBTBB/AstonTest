print('Введите числовой массив [n1, n2, n3, ...]')

s = input()
parse = s.strip('[]').replace(' ','').split(',')  #Преобразование в список из строковых значений
a = list(map(int, parse)) #Преобразование списка строковых значений в список числовых
b = []
for i in range(len(a)):
    if a[i] % 3 == 0:
        b.append((a[i]))
c = list(map(str, b))
print('Во введенном массиве следующие числа кратны трем:', ', '.join(c))
input('Нажмите Enter для выхода\n')

