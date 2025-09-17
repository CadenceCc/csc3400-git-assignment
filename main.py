from calculator import add, subtract, multiply, divide, power, square_root

def main():
    while True:
        print("\nSelect operation: add, subtract, multiply, divide, power, sqrt, quit")
        choice = input("Enter operation: ").lower()
        if choice == "quit":
            break
        try:
            if choice == "sqrt":
                num = float(input("Enter number: "))
                print("Result:", square_root(num))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == "add":
                    print("Result:", add(num1, num2))
                elif choice == "subtract":
                    print("Result:", subtract(num1, num2))
                elif choice == "multiply":
                    print("Result:", multiply(num1, num2))
                elif choice == "divide":
                    print("Result:", divide(num1, num2))
                elif choice == "power":
                    print("Result:", power(num1, num2))
                else:
                    print("Invalid operation")
        except ValueError:
            print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()