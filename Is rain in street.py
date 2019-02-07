print('Идет ли на улице дождь?')
step1 = input()
if step1.lower() == 'нет':
    print('Можно смело выходить погулять.')
elif step1.lower() == 'да':
    
    print('У вас есть зонт?')
    zont = input()
    if zont.lower() == 'да':
        print('Можно смело выходить погулять.')
    elif zont.lower() == 'нет':
        print('Нужно немного выждать')
    print('Дождь всё ещё идет?')
    da = input()
    if da.lower() == 'да':
        print('Нужно немного выждать')
    elif da.lower() == 'нет':
        print('Можно смело выходить погулять.')

print(input('Для выхода нажмите Enter. Приятной прогулки.'))
