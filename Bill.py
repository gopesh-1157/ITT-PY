print("Mad_Man supermarket\ndiscount 20% for more than 5000 purchase\ndiscount 10% for more than 3000 purchase")
amt=int(input("enter purchase amount:"))
if amt>=5000:
   print("BILL___$",amt,"\n20% discount\n$",(amt-(amt*0.2)))
elif amt>=3000 and amt<5000:
   print("BILL___$",amt,"\n10% discount\n$",(amt-(amt*0.1)))
else:
   print("BILL___$",amt)
