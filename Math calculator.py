
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("=" * 40)
print("      MATHEMATICAL CALCULATOR (MC)")
print("=" * 40)
print(" +   Addition")
print(" -   Subtraction")
print(" *   Multiplication")
print(" /   Division")
print(" \\   Integer Division")
print(" ^   Power")
print(" %   Modulus (remainder)")
print(" C   Clear screen")
print(" OFF Exit calculator")
print("=" * 40)

while True:
    operator = input("\nEnter operator (+ - * / \\ ^ % C OFF): ").strip()

    if operator.upper() == "OFF":
        print("\nCalculator switched OFF. Goodbye!")
        break

    elif operator.upper() == "C":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 40)
        print("      MATHEMATICAL CALCULATOR (MC)")
        print("=" * 40)
        print(" +   Addition")
        print(" -   Subtraction")
        print(" *   Multiplication")
        print(" /   Division")
        print(" \\   Integer Division")
        print(" ^   Power")
        print(" %   Modulus (remainder)")
        print(" C   Clear screen")
        print(" OFF Exit calculator")
        print("=" * 40)
        continue

    elif operator not in ['+', '-', '*', '/', '\\', '^', '%']:
        print("Invalid choice. Please select a valid operator.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered. Try again.")
        continue

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Error: Division by zero!"
        else:
            result = num1 / num2
    elif operator == '\\':
        if num2 == 0:
            result = "Error: Division by zero!"
        else:
            result = num1 // num2
    elif operator == '^':
        result = num1 ** num2
    elif operator == '%':
        if num2 == 0:
            result = "Error: Modulus by zero!"
        else:
            result = num1 % num2

    print(f"\nResult: {num1} {operator} {num2} = {result}")