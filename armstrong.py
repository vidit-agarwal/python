while (1):
    a = int(input("enter the number"))
    p=a//100
    q=a%100
    r=q//10
    s=q%10
    value =((p**3) + (r**3) + (s**3) )
    print (value)
    if value is a :
        print("\n number is  armstrong")
        break

    else :
        print("number is not armstrong")


