P=int(input("Enter the principle amount"))
T=int(input("time"))
R=int(input("rate of interest"))

if(R == 0):
    print("Simple_Interest is zero")
else:
    Simple_Interest=(P*T*R)/100
    print(Simple_Interest)

