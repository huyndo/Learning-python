leave_day = int(input("In what day do you leave? "))
duration = int(input("How long do you stay for? "))

return_day = (leave_day + duration) % 7
print("You return on ", return_day)