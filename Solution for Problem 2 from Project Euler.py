"""
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
        
