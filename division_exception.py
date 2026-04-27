try:
    a, b = map(int, input().split())

    if b==0:
        raise ZeroDivisionError
    
    print(f"div of a and b is {a/b}")
except ValueError:
    print("use integer type only ")
except ZeroDivisionError:
    print("division by zero not allowed")
