t1=input("enter time 1:")
t2=input("enter time 2:")

sec1=int(t1[11:13])*3600+int(t1[14:16])*60+int(t1[17:19])
sec2=int(t2[11:13])*3600+int(t2[14:16])*60+int(t2[17:19])

print(f"difference is :{sec2-sec1}")
