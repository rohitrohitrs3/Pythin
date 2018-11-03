num=eval(input("Enter the number : "))
multiplier = eval(input("Enter the multiplier : "))

if not (num< 50 and num%multiplier == 0):
    print("enter Number", num, "is a multiple of", multiplier)
else:
    print("enter Number", num, "is not multiple of number", multiplier)