def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print("Sum is", sum)

input_number = input("Enter integers separated by spaces: ").split()
input_number = [int(num) for num in input_number]
add(*input_number)