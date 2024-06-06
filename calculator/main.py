# calculator/main.py

from calculator.operations import add, subtract, multiply, divide

def calculator():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    while True:
        choice = input("Ingrese su opción (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            
            next_calculation = input("¿Quieres realizar otra operación? (sí/no): ")
            if next_calculation.lower() != 'sí':
                break
        else:
            print("Opción inválida, por favor selecciona una opción válida")

if __name__ == "__main__":
    calculator()
