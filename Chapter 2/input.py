name = input("Please enter your name: ")
print("Hello ", name)

# seconds conversion using input
sec = int(input("Please enter total seconds "))
minutes = sec // 60
sec = sec % 60
hour = minutes // 60
minutes = minutes % 60
print(hour, "h ", minutes, " min", sec , " s")