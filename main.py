import calculator

def main():
    print("Welcome to the Calculator!")
    print("Available operations: add, subtract, multiply, divide, power, square_root")
    
    while True:
        operation = input("\nEnter operation (or 'quit' to exit): ").strip()
        if operation == "quit":
            print("Goodbye!")
            break

        if operation == "square_root":
            try:
                num = float(input("Enter a number: "))
                print("Result:", calculator.square_root(num))
            except ValueError:
                print("Error: Invalid input")
        else:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if operation == "add":
                    print("Result:", calculator.add(a, b))
                elif operation == "subtract":
                    print("Result:", calculator.subtract(a, b))
                elif operation == "multiply":
                    print("Result:", calculator.multiply(a, b))
                elif operation == "divide":
                    print("Result:", calculator.divide(a, b))
                elif operation == "power":
                    print("Result:", calculator.power(a, b))
                else:
                    print("Error: Unknown operation")
            except ValueError:
                print("Error: Invalid input")

if __name__ == "__main__":
    main()