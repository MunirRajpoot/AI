# even_odd_check.py

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    user_input = int(input("Please enter an integer: "))
    result = check_even_odd(user_input)
    print(f"The number {user_input} is {result}.")

if __name__ == "__main__":
    main()
