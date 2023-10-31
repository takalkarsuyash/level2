def fibonacci(n):
    a, b = 0, 1
    print(a, b, end=" ")
    for i in range(n - 2):
        c = a + b
        print(c, end=" ")
        a, b = b, c
n = int(input("Enter the number of terms:"))
fibonacci(n)
