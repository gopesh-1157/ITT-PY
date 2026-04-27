n=int(input("Enter the number :"))
s =0
for i in range(1,n+1):
   if i%2==0:
        s+=1
print("count of even numbers upto",n,"is ",s)
