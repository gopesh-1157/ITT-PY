amount=int(input("enter the purchase amount:"))
if amount>=5000:
   d_amount=amount*0.02
   amount-=d_amount
elif 5000>=amount>=3000:
    d_amount=amount*0.01
    amount-=d_amount
else:
    print("enter valid amount")

print("bill amount",amount)
