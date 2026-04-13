a=int(input('enter no of coins for suresh:'))
b=int(input('enter no of coins for sundar:'))
c=int(input('enter no of coins for raja:'))
d=int(input('enter no of coins for suresh:'))
if a>b:
   b=b+c
   if a>b:
      b=b+d
      if a>b:
         winner='suresh'
      else:
         winner='sundar'
   else:
      a=a+d
      if b>a:
         winner='sundar'
      else:
         winner='suresh'
else:
   a=a+c
   if a>b:
      b=b+d
      if a>b:
         winner='suresh'
      else:
         winner='sundar'
   else:
      a=a+d
      if b>a:
         winner='sundar'
      else:
         winner='suresh'
print('winner is :',winner)
