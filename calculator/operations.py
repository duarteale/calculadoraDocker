# calculator/operations.py

def add(x, y):
    """Suma"""
    return x + y

def subtract(x, y):
    """Resta"""
    return x - y

def multiply(x, y):
    """Multiplicación"""
    return x * y

def divide(x, y):
    """División"""
    if y == 0:
        return "Error: División por cero"
    return x / y
