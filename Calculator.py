
# calculator 

def addition(number_1, number_2):
    answer = number_1 + number_2
    print(f" = {answer}")

def subtraction(number_1, number_2):
    answer = number_1 - number_2
    print(f" = {answer}")

def multiplication(number_1, number_2):
    answer = number_1 * number_2
    print(f" = {answer}")

def division(number_1, number_2):
    if number_2 == 0:
        print("Cannot divide by zero!")
    
    else:
        answer = number_1 // number_2
        print(f" = {answer}")

def display_menu():
    print("______ Calculator_____")
    print("\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def main():
    
    display_menu()
    user_option = int(input("Enter your option: "))

    if user_option == 1:
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        addition(number_1, number_2)
    
    elif user_option == 2:
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        subtraction(number_1, number_2)

    elif user_option == 3:
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        multiplication(number_1, number_2)

    elif user_option == 4:
        number_1 = int(input("Enter a number: "))
        number_2 = int(input("Enter another number: "))
        division(number_1, number_2)

    elif user_option == 5:
        print("Thank you")

    else:
        print("Invalid option entered")

main()