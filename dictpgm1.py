students={
    "Anu":340,
    "Teena":560,
    "John":300
}
asc_by_name=dict(sorted(students.items()))
print("sorted by name(Ascending):")
print(asc_by_name)

desc_by_name=dict(sorted(students.items(),reverse=True))
print("\nsorted by name(Descending):")
print(desc_by_name)

