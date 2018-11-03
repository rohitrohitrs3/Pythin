##Calculate Simple_Inrerest using evaluate operator

P=eval(input("Enter Principle amount : "))
T=eval(input("time of interest : "))
R=eval(input("rate of interest :"))

if (R == 0):

    print("interest is zero")

else:

    Simple_Interest= (P*R*T)/100

    print(Simple_Interest)


