# dictionaries consists of {"key" : "value"} ie Country:Capital city
# No duplicates allowed 

students = {"Allan":"001",
            "Ian":"002",
            "Kuria":"003",
            }

# to get the value of a particular key
print(students.get("Allan"))

# to update/change the dictionary
students.update({"Telvin":"004"})
students.update({"Telvin":"005"})
print(students)

# to remove a key
print(students.pop("Allan"))

# to iterate over the dictionary
for key in students.keys():
    print(key)

for value in students.values():
    print(value)

# to iterate over the dictionaries items without splitting 
for keys, values in students.items():
    print(f"{keys}:{values}") 
