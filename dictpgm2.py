contacts1={
    "Anu":"9887765634",
    "Teena":"9887765639"
}

contacts2={
    "adarsh":"9887765644",
    "abhinav":"9887765679"
}
print("contact1:",contacts1)
print("contact2:",contacts2)

merged_contacts=contacts1.copy()
merged_contacts.update(contacts2)

print("merged_contacts:")
print(merged_contacts)