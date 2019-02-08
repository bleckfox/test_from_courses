lst = [-8, 7, 5, -2, 3, -4, 2, -6]
def closeToZero(li):
    try:
        num = li[0]
        for e in li:
            if abs(e) == abs(num):
                if e > num: num = e
            elif abs(num) > abs(e): num = e
    except:
        print('Error')
    finally:
        print(num)
closeToZero(lst)
