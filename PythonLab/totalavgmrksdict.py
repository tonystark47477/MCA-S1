students={
    "Anu": [85,90,78],
    "Reena": [72,88,91],
    "John": [95,80,85]
}
for name, marks in students.items():
    total=sum(marks)
    average=sum(marks)/len(marks)
    print(f"Students: {name}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print("." * 20)