num =int(input("Number please:"))
def factorial(n):
    x = 1
    for i in range(n):
        x = x * (n - i)
    return x
print (factorial(num))

