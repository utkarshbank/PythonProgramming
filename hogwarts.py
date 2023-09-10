
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }
enterName =  input("Enter a Name: ")
if enterName in students:
    print(students[enterName])
else:
    print("Name does not exist")