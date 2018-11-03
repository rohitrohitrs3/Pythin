n=eval(input("Enter the Number : "))

if(not isinstance(n,int)):
    print("Wrong Input")
else:
    if(n%7==0):
        print("Multiple of 7")
    else:
        print("not multiple of 7")

