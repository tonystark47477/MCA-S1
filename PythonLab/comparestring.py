def compare(s1, s2, n):
    count = 0
    limit = min(n, len(s1), len(s2))
    for i in range(limit):
        if s1[i] == s2[i]:
            count += 1
    return "true" if count == limit and limit == n else "false"

s1 = input("Enter the string1: ")
s2 = input("Enter the string2: ")
n = int(input("Enter the number: "))
print("The first", n, "characters of both strings are the same?:", compare(s1, s2, n))
