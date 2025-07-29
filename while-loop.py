
# name = input("Enter your name: ")

# while name == "":
#     name = input("Enter your name: ")

# print(f"Hello {name}")

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than 0")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate must be greater than 0")

while time <= 0:
    time = float(input("Enter the time: "))
    if time <= 0:
        print("Time must be greater than 0")


total_amount = principal * pow(1 + rate/100, time)
print(f"Balance after {time} years is {total_amount:.2f}")

#break statement
