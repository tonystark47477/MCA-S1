n = int(input("Enter the limit: "))
a, b = 0, 1
print("Fibonacci series up to", n, "terms:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b