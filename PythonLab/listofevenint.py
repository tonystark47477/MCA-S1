nums = list(map(int, input("Enter a list of integers separated by spaces: ").split())) 
result = [] 
for n in nums: 
    if n % 2 != 0:   
        result.append(n) 
print("Entered numbers:", nums) 
print("List after removing even numbers:", result)