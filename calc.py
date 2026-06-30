# calc.py
def main():
    print("--- Simple Calculator ---")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    addition = num1 + num2
    print(f"Addition: {num1} + {num2} = {addition}")

if __name__ == "__main__":
    main()