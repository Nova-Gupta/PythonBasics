def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
def subtract(a, b):
    return a - b
result = add(2,5)
print(result)
result = subtract(10,4)
print(result)
result = multiply(3,7)
print(result)
result = divide(8,2)
print(result)