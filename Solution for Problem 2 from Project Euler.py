# Суть в сохранении предыдущих значений в списке, чтобы заново их не вычислять
n = int(input())
l = [0, 1]
for i in range(n):
    l.append(l[-1]+l[-2])
if len(l) == 3:
    print('1')
else:
    for i in l[1:-1]:
        print(i, end=' ')

"""
Этот код не работает
#Числа Фибоначчи
R = int(input())
F0 = 0
F1 = 1
total = 0
for i in range(0,R):
    F0, F1 = F1, F0 + F1
    #print(F0)
    #проверяю четность
    if F0 % 2 == 0:
        #print(F0)
    #складываю(+) четные значения
        total = total + F0
print(total)
#при таком алгоритме время выполнения программы более 24 минут
#прошло 24 минуты 08 секунд, и ответ не был получен
"""
        
