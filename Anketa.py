"""
Запросить у пользователя данные в форме анкеты ;
Полученные данные записать в файл .txt ;
Открыть файл, изменить данные.
ограничение на количество попыток и возврат в начало
"""
#NameList = [Name, SurName, Age, Sex, Country, City, Married, Child, Job]
def Name():
    while True:
        Name = str(input('Имя:  '))
        if Name.isalpha() == True:
            return Name
            break
        else:
            print('Имя пишут буквами, и без кавычек :)')
            continue

def SurName():
    while True:
        SurName = str(input('Фамилию:  '))
        if SurName.isalpha() == True:
            return SurName
            break
        else:
            print('Фамилию пишут буквами, и без кавычек :)')
            continue

def Age():
    while True:
        try:
            Age = int(input('Возраст:  '))
            if type(Age) == int:
                return Age
                break
        except (ValueError):
            print('Нужно число :)')
            continue


name = Name()
print('Your name is ', name)
surName = SurName()
print('Your surname is ', surName)
age = Age()
print('Your age is ', age)
List = []
List.append(name)
List.append(surName)
List.append(age)
print(List)
i='Имя: '
f='фамилия: '
v='Возраст: '
dataS = {
    i: name,
    f: surName,
    v: age
    }
datas = str(dataS)
file = open('data.txt', 'w')
file.write(datas)
file.close()

input('Для выхода нажмите любую клавишу... ')
