# calc.py
def main():
    print("--- Simple Calculator ---")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    addition = num1 + num2
    multiplication = num1 * num2
    
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")


if __name__ == "__main__":
    main()
