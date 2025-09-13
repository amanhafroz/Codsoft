n1 = float(input("Enter the number : "))
n2 = float(input("Enter the number : "))

print("Choose the operation +, *, /, -")
operation = input("Enter the operation : ")

if operation == "+":
    print("Additon of both numbers",n1+n2)

elif operation == "*":
    print("Multiplication of both numbers",n1*n2)

elif operation == "-":
    print("Subtraction of both numbers",n1-n2)

elif operation == "/":
    if n2 != 0 :
        print("Division of both numbers",n1/n2)
    else:
        print("Not Division by zero")