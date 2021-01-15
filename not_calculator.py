#These functions calculate up to 4 numbers
def add(x, y, z, v):
    return x + y + z + v

def subtract(x, y, z, v):
    return x - y - z - v

def multiply(x, y, z, v):
    return x * y * z * v

def divide(x, y, z, v):
    return x / y / z / v

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))

        # Receive
        if choice == '1':
            print(num1, "+", num2, "+", num3, "+", num4, "=", add(num1, num2, num3, num4))

        elif choice == '2':
            print(num1, "-", num2, "-", num3, "-", num4, "=", subtract(num1, num2, num3, num4))

        elif choice == '3':
            print(num1, "*", num2, "*", num3, "*", num4, "=", multiply(num1, num2, num3, num4))

        elif choice == '4':
            print(num1, "/", num2, "/", num3, "/", num4, "=", divide(num1, num2, num3, num4))
        break

while True:
    # Take additional input from the user
    question = input("Would you like to make another calculation[y/n]?\n")

    while question != 'n':
        if question == 'y':

            choice = input("Enter choice(1/2/3/4): ")

            # Check if choice is one of the four options
            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                num3 = float(input("Enter third number: "))
                num4 = float(input("Enter fourth number: "))

                # Receive
                if choice == '1':
                    print(num1, "+", num2, "+", num3, "+", num4, "=", add(num1, num2, num3, num4))

                elif choice == '2':
                    print(num1, "-", num2, "-", num3, "-", num4, "=", subtract(num1, num2, num3, num4))

                elif choice == '3':
                    print(num1, "*", num2, "*", num3, "*", num4, "=", multiply(num1, num2, num3, num4))

                elif choice == '4':
                    print(num1, "/", num2, "/", num3, "/", num4, "=", divide(num1, num2, num3, num4))
                break

    while question != 'y':
        if question == 'n':

            print("Goodbye!")
