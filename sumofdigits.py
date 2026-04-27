n=int(input("enter a number :"))
t=n
s=0
while t>0:
   rem=t%10
   s+=rem
   t//=10
print("sum of the digit of the number",n,"is",s)
