def fib_seq_iterative(n):
    if n == 1:
        print(0)
    elif n==2:
        print(0,1)
    else:
        print(0,1, end=" ")
        a, b = 0, 1
        for i in range(1,n-1):
            print(a+b, end=" ")
            a, b = b, a+b
    print()

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fib_seq_recursive(n):
    for i in range(0, n):
        print(fibonacci(i), end=" ")


print("First 25 fibonacci terms using iterative method: ",fib_seq_iterative(25))
print("First 25 fibonacci terms using recursive: ",fib_seq_recursive(25))

