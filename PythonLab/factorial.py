num = int(input("Enter a number: "))
fact = 1
for i in range(2, num + 1):
    fact *= i
print("The factorial of", num, "is", fact)