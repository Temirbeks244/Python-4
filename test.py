a = float(input("Sankirgiz: "))
b = float(input("Sankirgiz: "))

c = input("1,2,3,4: ")

if c == "1":
    print(a+b)
elif c == "2":
    print(a-b)
elif c == "3":
    print(a*b)
elif c == "4":
    if b != 0:
        print(a/b)
    else:
        print("Nolgo boluugo bolboit!")
else:
    print("Tuura emes tandoo!")