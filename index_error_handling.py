try:
    list=input("enter elements :").split()
    n=int(input("enter the index:"))
    print(f"element at index {n} id {list[n]}")
except IndexError:
    print("index out of bounds ") 
except ValueError:
    print("use integer type only ")
