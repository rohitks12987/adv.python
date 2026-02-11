#1) Create a dictionary and print all key–value pairs
student = {"name": "Rohit", "age": 21, "course": "BCA"}

for key, value in student.items():
    print(key, ":", value)

#2) Access a value using a key
student = {"name": "Rohit", "age": 21}
print(student["name"])

#3) Add a new key–value pair
student = {"name": "Rohit", "age": 21}
student["city"] = "Delhi"
print(student)

#4) Update an existing key value
student = {"name": "Rohit", "age": 21}
student["age"] = 22
print(student)

#5) Delete a key using pop() and display removed value
student = {"name": "Rohit", "age": 21}
removed = student.pop("age")
print("Removed value:", removed)
print(student)

#6) Iterate through keys and values using a loop
student = {"name": "Rohit", "age": 21, "city": "Delhi"}

for key in student:
    print(key, ":", student[key])

#7) Check whether a key exists in a dictionary
student = {"name": "Rohit", "age": 21}

if "name" in student:
    print("Key exists")
else:
    print("Key not found")

#8) Count the number of keys in a dictionary
student = {"name": "Rohit", "age": 21, "city": "Delhi"}
print("Total keys:", len(student))

#9) Create a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Rohit", 21, "Delhi"]

data = dict(zip(keys, values))
print(data)

#10) Find the sum of all values in a dictionary
marks = {"math": 80, "science": 70, "english": 90}
print("Sum:", sum(marks.values()))

#11) Find the key with the maximum value
marks = {"math": 80, "science": 95, "english": 90}

max_key = max(marks, key=marks.get)
print("Key with max value:", max_key)

#12) Reverse keys and values
data = {"a": 1, "b": 2, "c": 3}

reversed_dict = {v: k for k, v in data.items()}
print(reversed_dict)

#13) Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)

#14) Remove duplicate values
data = {"a": 1, "b": 2, "c": 2, "d": 3}

unique = {}
for k, v in data.items():
    if v not in unique.values():
        unique[k] = v

print(unique)

#15) Dictionary with numbers and their squares
squares = {x: x*x for x in range(1, 6)}
print(squares)

#16) Sort a dictionary by keys
data = {"b": 2, "a": 1, "c": 3}

sorted_dict = dict(sorted(data.items()))
print(sorted_dict)

#17) Sort a dictionary by values
data = {"a": 3, "b": 1, "c": 2}

sorted_dict = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_dict)

#18) Create a nested dictionary and access inner values
student = {
    "s1": {"name": "Rohit", "age": 21},
    "s2": {"name": "Amit", "age": 22}
}

print(student["s1"]["name"])

#19) Use get() method and explain advantage
student = {"name": "Rohit", "age": 21}

print(student.get("name"))
print(student.get("city", "Not Found"))

#20) Count frequency of characters in a string
text = input("Enter a string: ")
freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
