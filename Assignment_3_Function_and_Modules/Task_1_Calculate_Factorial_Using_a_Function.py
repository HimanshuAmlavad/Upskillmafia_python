def Factorial(num):

    if num < 2:
        return 1
    return num * (Factorial(num-1))

num = int(input("Enter the number: "))
ans = Factorial(num)
print("Factorial of",num,"is: ",ans)