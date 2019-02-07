a, b, c, d = int(input()), int(input()), int(input()), int(input())


while a<=10 and b<=10 and c<=10 and d<=10:
  LIST = []
  
  for e in range(c,d+1):
    LIST.append(e)
    print(' ' + '\t' + str(e), end='')
    
  print()
  
  for y in range(a,b+1):
    print(y, end='\t')
    for i in LIST:
      print(y*i, end='\t')
      
    print()
    
  print()
  print(LIST)
  break
else:
  print('number more than 10')
