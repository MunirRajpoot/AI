# simple_division.py

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
