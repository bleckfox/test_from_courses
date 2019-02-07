def collatz(n):
    sp = [n]
    if n<1:
        return []
    while n>1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        sp.append(n)
    for i in sp:
        print(i, end=' ')

collatz(int(input()))
