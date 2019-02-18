time = int(input("Please enter your time in hours: "))
wait = int(input("How long do you want before the alarm goes off? "))

alarm_time = (time + wait) % 24
print("Alarm goes off at ", alarm_time)