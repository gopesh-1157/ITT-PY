t=int(input("iterations :"))
total=[]
for _ in range(t): 
    x=int(input("enter the x :"))
    res=input("enter the result :")
    chandru=0
    nirmal=0
    for i in res:
        if i=="C":
            chandru+=2
        elif i=="N":
            nirmal+=2
        else:
            chandru+=1
            nirmal+=1

    if chandru>nirmal:
        total.append(60*x)
    elif nirmal>chandru:
        total.append(40*x)
    else:
        total.append(55*x)
       
for i in total:
    print(i)
