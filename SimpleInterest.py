p=int(input("enter the principal amount :"))
r=int(input("enter the rate of interest :"))
t=int(input("enter the time period :"))
if (1<=p<=100000 and 1<=r<=20 and 1<=t<=10):
   a=p*r*t;
   b=a/100;
   print("Simple interst" ,b)
else:
   print("invalid")
