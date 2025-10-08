students={
    "Anu": 340,
    "Reena": 458,
    "John": 300
}
asc_by_name = dict(sorted(students.items()))
print("Sorted by name (Ascending):")
print(asc_by_name)
desc_by_name=dict(sorted(students.items(),reverse=True))
print("Sorted by name (Descending):")
print(desc_by_name)