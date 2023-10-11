#creating a list of dictionaries
group = [{"name": "James", "age": 57},
         {"name": "Moses", "age": 25},
         {"name": "Alice", "age": 36}]

#printing and sorting by the age
print(sorted(group, key=lambda i: i["name"]))

#printing and sorting by the age
print(sorted(group, key=lambda i: i["age"]))

#printing and sorting by nanme and age
print(sorted(group, key=lambda i: (i["age"], i["name"])))