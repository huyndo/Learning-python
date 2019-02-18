P = 10000
n = 12
r = 0.08
t = int(input("How long will be money be in the bank? "))

final = P * (1 + r / n) ** (n * t)
print("The money collected is: ", final)