t=int(input("enter time t:"))
m_tot=int(input("enter total minute m total:"))
numarator=(3*m_tot -10*t)

if m_tot<60 or (m_tot%10 !=0) or t>=m_tot or (numarator %170 !=0):
    print("invalid")
else:
    h=numarator//170
    m=t-h
    if h<0 or m<0:
        print("invalid")
    else:
        print(f"H = {h} , M = {m}")
