t=int(input("enter time t :"))
h_tot=int(input("enter total time :"))
if h_tot<24 or (h_tot&1 ==1 ) or t>=h_tot:
    print("invalid input !")
else:
    d=(h_tot-18*t)//6
    h=t-d
    if d<0 or h<0:
        print("invalid input !")
    else:
        print(f"d: {d} and h :{h}")
