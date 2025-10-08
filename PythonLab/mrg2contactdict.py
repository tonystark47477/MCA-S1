contacts1={
    "Anu":"9876543210",
    "Teena":"8765432109"
}
contacts2={
    "John":"1234567890",
    "Priya":"9821435487"
}
print("Contact1:",contacts1)
print("Contact2:",contacts2)
merged_contacts=contacts1.copy()
merged_contacts.update(contacts2)
print("Merged Contacts:")
print(merged_contacts)
