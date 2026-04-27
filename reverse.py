n=int(input("enter a number :"))
t=n
rev=0
while t>0:
   rem=t%10
   rev= (rev*10) + rem
   t//=10
print("reverse of the number",n,"is",rev)
