file = open("file2.txt","w")
file.write("hello world!\n Welcome to python programming\n Thank you")
file.close()
list = []
file = open("file2.txt","r")
list = [line.strip() for line in file]
file.close()
print(list)