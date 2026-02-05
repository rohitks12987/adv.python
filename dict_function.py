student = {
    "name": "Rohit",
    "age": 21,
    "course": "CSE"
}

print("Original Dictionary:")
print(student)
print("-" * 40)

# 1. keys()
print("Keys:")
print(student.keys())
print("-" * 40)

# 2. values()
print("Values:")
print(student.values())
print("-" * 40)

# 3. items()
print("Items (key-value pairs):")
print(student.items())
print("-" * 40)

# 4. get()
print("Get age:")
print(student.get("age"))
print("Get city (key not present):")
print(student.get("city"))   # No error
print("-" * 40)

# 5. update()
print("After update():")
student.update({"age": 22, "city": "Bhubaneswar"})
print(student)
print("-" * 40)

# 6. pop()
print("After pop('course'):")
student.pop("course")
print(student)
print("-" * 40)

# 7. popitem()
print("After popitem():")
student.popitem()
print(student)
print("-" * 40)

# 8. copy()
print("Copy of dictionary:")
student_copy = student.copy()
print(student_copy)
print("-" * 40)


