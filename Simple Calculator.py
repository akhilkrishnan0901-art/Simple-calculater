print('''
     + addition
     _ subtraction
     * multiplication
     / division''')
a=int(input("Enter the value 1 :"))
b=int(input("Enter the value 2 :"))
opr=input("Enter the operator :")
if opr=="+":
    print(a+b)
elif opr=="-":
    print(a-b)
elif opr=="*":
    print(a*b)
elif opr=="/":
    print(a/b)
else:
    print("Invalid Number")