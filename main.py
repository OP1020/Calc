def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    #TODO: You handle * and / with more elif
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

# Test cases
print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '-'))  # Output: 5
print(calculator(10, 5, '*'))  # Output: 50
print(calculator(10, 5, '/'))  # Output: 2.0