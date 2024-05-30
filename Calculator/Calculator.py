def Addition(x, y):
    return x + y


def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y


def Division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "can't divide by zero"


def Modulus(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "can't divide by zero"


def main():
    print("Simple Calculator")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Modulus")

    while True:

        choice = int(input("Enter your Choice(1/2/3/4/5) : "))
        if choice in range(1, 6):
            num1 = float(input("Enter the first number : "))
            num2 = float(input("Enter the second number : "))

            match choice:
                case 1:
                    result = Addition(num1, num2)
                case 2:
                    result = Subtraction(num1, num2)
                case 3:
                    result = Multiplication(num1, num2)
                case 4:
                    result = Division(num1, num2)
                case 5:
                    result = Modulus(num1, num2)

            print(f"Result: {result}")

        else:
            print("Invalid Choice input")

        nextCalculation = input("Do you want to perform another calculation? (yes/no) : ")
        if nextCalculation.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
