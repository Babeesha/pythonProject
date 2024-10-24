def biggest(a,b):
    if a>b:
        return a
    if b>a:
        return b
    
    a=int(input("Enter 'a' value:"))
    b=int(input("Enter 'b' value:"))
    #function call
    big=biggest(a,b)
    print("big number=", big)