a = int(input("Enter Basic pay:"))
if(5000<=a<=50000):
	print(f"Basic Pay:{a+0.2*a+0.1*a}")
else:
	print("invalid")
