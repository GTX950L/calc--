"""
🧮 CLI Calculator
A simple command-line calculator supporting +, -, *, /

Run: python calculator.py
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def main():
    print("=" * 40)
    print("    🧮  Simple Calculator")
    print("=" * 40)
    print("Operations: +  -  *  /  (type 'quit' to exit)")
    print("-" * 40)

    while True:
        # Get user input
        expression = input("\nEnter calculation (e.g. 5 + 3): ").strip()

        if expression.lower() == 'quit':
            print("Goodbye! 👋")
            break

        if not expression:
            continue

        # Parse: split into number, operator, number
        parts = expression.split()
        if len(parts) != 3:
            print("Invalid format. Use: number operator number (e.g. 5 + 3)")
            continue

        try:
            num1 = float(parts[0])
            op = parts[1]
            num2 = float(parts[2])
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        # Calculate
        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print(f"Unknown operator: '{op}'. Use +, -, *, or /")
            continue

        # Show result
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
