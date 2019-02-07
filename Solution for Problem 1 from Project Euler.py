total = 0
count = 0               
R = int(input())        #прошу ввести число
while count < R:        
    count = count + 1   #увеличиваю значение на 1
    #print(count)
                        #дальше в 'if' проверяю кратность числа
                        #% - остаток от деления
                        #== - проверка равенства
                        
    if count % 5 == 0 and count < R  or count % 3 == 0 and count < R:
        #print(count)
        total = total + count  #складываю(+) результаты проверки
        print(total)           #total=0+3; total=3+5; total=8+6 etc.
"""
Второй вариант программы.
Сразу выдает результат, без вывода промежуточных значений.
total = 0
count = 0               
R = int(input())        #прошу ввести число
while count < R:        
    count = count + 1   #увеличиваю значение на 1
    #print(count)
                        #дальше в 'if' проверяю кратность числа
                        #% - остаток от деления
                        #== - проверка равенства
                        
    if count % 5 == 0 and count < R  or count % 3 == 0 and count < R:
        #print(count)
        total = total + count  #складываю(+) результаты проверки
print(total)           #total=0+3; total=3+5; total=8+6 etc.
"""
