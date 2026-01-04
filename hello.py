print("🧮 Calculator")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose an operation:")
        print(" +  for addition")
        print(" -  for subtraction")
        print(" *  for multiplication")
        print(" /  for division")

        operation = input("Enter operation: ")

        if operation == "+":
            print("Result:", num1 + num2)

        elif operation == "-":
            print("Result:", num1 - num2)

        elif operation == "*":
            print("Result:", num1 * num2)

        elif operation == "/":
            if num2 == 0:
                print("❌ Error: Cannot divide by zero")
            else:
                print("Result:", num1 / num2)

        else:
            print("❌ Invalid operation")

    except ValueError:
        print("❌ Error: Please enter valid numbers")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Goodbye!")
        break
