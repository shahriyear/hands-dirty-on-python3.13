
op = input("Enter an operator (+, -, *, /): ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(num1 / num2)
else:
    print("Invalid operator")