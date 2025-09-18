from calculator import add, subtract, multiply, divide, power, square_root

# Test 1: add
print("Add 2 + 3 =", add(2, 3))  # Expected: 5

# Test 2: subtract
print("Subtract 5 - 2 =", subtract(5, 2))  # Expected: 3

# Test 3: multiply
print("Multiply 4 * 3 =", multiply(4, 3))  # Expected: 12

# Test 4: divide (including division by zero)
print("Divide 10 / 2 =", divide(10, 2))  # Expected: 5
print("Divide 10 / 0 =", divide(10, 0))  # Expected: Error: Cannot divide by zero

# Test 5: square root (including negative number)
print("Square root of 16 =", square_root(16))  # Expected: 4
print("Square root of -4 =", square_root(-4))  # Expected: Error: Cannot take square root of negative number