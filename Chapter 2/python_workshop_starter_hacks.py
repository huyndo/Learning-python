print("Hello World!")
favColour = input("What is your favorite colour?")
print("The user's favourite colour is: " + favColour)

print(9 + 10)
print(12 / 3)

number = int(input("Giff a number"))
if number > 0:
    print("This is a positive number")
elif number == 0:
    print("This is a non-signed number")
else:
    print("This is a negative number")

ingredients = ["jam"]
ingredients.append("Eggs")
print(ingredients)
ingredients.remove("jam")
print(ingredients)