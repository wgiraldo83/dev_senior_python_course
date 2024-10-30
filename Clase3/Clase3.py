age = int(input("How old are you? "))
country = "USA"
userHasDNI = True

""" Conditional if"""

if age >= 21 and country == "USA":
    print("You can buy alcohol")
elif age >= 18 and country == "Col":
    print("You can buy alcohol")
else:
    print("You can't buy alcohol")


""" Bocle For """
for student in range(10):
    print(student)


""" Bucle While """
while userHasDNI:
    age = int(input("Enter your age: "))
    country = input("Enter your country: ")
    if age >= 21 and country == "USA":
        print("You can buy alcohol in USA")
        break
    elif age >= 18 and country == "COL":
        print("You can buy alcohol in COL")
        break
    elif age >= 16 and country == "GER":
        print("You can buy alcohol in GER")
        break
    else:
        userHasDNI = False
        print("You can't buy alcohol")
