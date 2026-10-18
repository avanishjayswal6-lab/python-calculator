# ==========================================
# Simple CLI Calculator in Python
# Author: Avanish Jayswal
# ==========================================

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function with zero-check"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def main():
    print("=" * 35)
    print("      PYTHON CALCULATOR APP       ")
    print("=" * 35)
    
    while True:
        print("\nSelect Operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        # Check if user wants to exit
        if choice == '5':
            print("\nThank you for using the Calculator! Goodbye.")
            break
            
        # Valid choices check
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values only.")
                continue

            if choice == '1':
                print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("Invalid Selection! Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()