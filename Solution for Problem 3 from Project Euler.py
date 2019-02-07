forSolve = 600851475143
R = int(input())
e = 0
while e < R:
    e+=1
    if R % e == 0 and R > e:
        total = []
        total.append(e)
        print(total)
    
