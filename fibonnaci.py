# 9. Sum of first 50 Fibonacci numbers

# Fibonacci function using recursion
def fibonacci(n):
    sum = 0
    if n==1 or n==0:
        return 0
    a=0
    b=1
    sum += a+b

    for i in range(2, n):
        temp = a
        a = b
        b = temp+b
        sum += b

    return sum

SUM = fibonacci(50)
print("Sum of first 50 Fibonacci numbers: ", SUM)