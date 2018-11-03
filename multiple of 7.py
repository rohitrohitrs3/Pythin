n=eval(input("Enter the number : "))
multiplier = eval(input("Enter the multiplier"))
if(n > 50):
    print("Wrong Input !!")
elif(n%multiplier == 0):
    print("enter Number", n, "is a multiple of", multiplier)
else:
    print("enter Number", n, "is not multiple of number", multiplier)



