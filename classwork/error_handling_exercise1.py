def get_age():
    age = input("Enter your age: ")
    return int(age)

try:
    age = get_age()
except ValueError:
    print("Invalid age input.")
else:
    print("Your age is:", age)
