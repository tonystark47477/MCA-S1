file = open("file3.txt", "w")
file.write("This is the firstline\nThis is the secondline\nThis is the thirdline\nThis is the fourthline")
file.close()
file = open("file3.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
with open("file3.txt", "r") as file2:
    for line in file2:
        print(line.strip())