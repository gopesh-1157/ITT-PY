a=int(input("Enter a  number1:"))
b=int(input("Enter a  number2:"))
ch=int(input("Enter a  choice"))

match ch:
   case 1:
      print("addition ",a+b)
   case 2:
      print("subtraction",a-b)
   case 3:
      print("Multiplication",a*b)
   case 4:
      print("Division",a%b)
   case _:
      print("invalid")
