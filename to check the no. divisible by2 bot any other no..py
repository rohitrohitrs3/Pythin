# n=eval(input("Enter the number : "))
# if(isinstance(n, int)):
#     for i in range(0,n,2):
#       print(i)



n=eval(input("Enter the number : "))
if(isinstance(n, int)):
    for i in range(0,n,2):
        if(not i%3 == 0):
            print(i)
            for j in range(0,n,2):
                if(j%2 == 0):
                    # print(j)
                    print(i,j)
