def calculation():
    a = int(input("enter a value: "))
    b = int(input("enter b value: "))
    print("select an operation 1. add 2. sub 3. mul 4. divison")
    c = int(input())
    if c == 1:
        print(f"the sum is {a+b}")
    elif c == 2:
        print(f"the sub is {a-b}")
    elif c == 3:
        print(f"the mul is {a*b}")
    elif c == 4:
        print(f" {a}/{b} ={a/b} ")
    else:
        print("invalid")
calculation()
