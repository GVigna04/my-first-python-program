print("caluculator")
while True:
    try:

num1=float(input("enter first number"))
num2=float(input("enter second number"))

print("Choose an operation:")
print(" +  for addition")
print(" -  for subtraction")
print(" *  for multiplication")
print(" /  for division")

operation = input("enter operation")

if operation == "+":
    result = num1 + num2
    print("result:",result)

elif operation == "-":
    result = num1 - num2
    print("result:",result)

elif operation == "*":
    result = num1 * num2
    print("result:",result)

elif operation == "/":
    if num2 == 0:
       print("error: cannot divide by 0")
    else:
       result = num1 / num2
       print("result:", result)

else:
    print("Invalid operation")

except ValueError:
print("❌ Error: Please enter valid numbers")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Goodbye!")
        break

