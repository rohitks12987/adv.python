#employee details
#employee others details = keyword arguments
def EmploymentDetails(name, age, department="Chikiti", **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {department}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
EmploymentDetails("Vivek", 30, location="Bhubaneswar", salary=50000)